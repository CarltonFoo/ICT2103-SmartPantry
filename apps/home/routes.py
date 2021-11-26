from dns.rdatatype import NULL
from apps.home import blueprint
from flask import render_template, redirect, request, jsonify
from flask_login import (
    current_user, 
    login_required 
)
from jinja2 import TemplateNotFound
from Controls.queryControl import queryingOn
# temp
from Objects.sql_commands import mydb
from apps.authentication.util import hash_pass
from apps.authentication.models import Users, pantry

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>', methods=['GET', 'POST'])
@login_required
def route_template(template):
    
    try:
        
        if not template.endswith('.html'):
            template += '.html'
            
        if template == "profile.html":
            where = "username ='" + str(current_user) + "'"
            data = queryingOn(method="SELECT", selection="*", table_name="user", data=where)
        
        if template == "recipes.html":
            data = [("dummy data")]
            
        if template == "inventory.html":
            data = [("dummy data")]
            
        if template == "pricechecker.html":
            data = queryingOn(method="SELECT", selection="*", table_name="user")
            
        if template == "budgeting.html":
            data = [("dummy data")]
            
        if template == "history.html":
            data = [("dummy data")]
        
        if template == "aboutus.html":
            data = [("dummy data")]


        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, data=data)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/updateprofile', methods=['GET', 'POST'])
@login_required
def saveDetails():
    print("Updating profile...")
    try: 
        if request.method == 'POST':
            if request.form['username']:
                user = Users.query.filter_by(username=request.form['username']).first()
                if not user:
                    username = str(request.form['username'])
                    height = str(request.form['height'])
                    weight = str(request.form['weight'])
                    age = str(request.form['age'])
                    gender = str(request.form['gender'])
                    bio = str(request.form['bio'])
                    diet = str(request.form['diet'])
                    
                    sql = 'UPDATE user SET username = "' + username + '", height = ' + height + ', weight = ' + weight + ', age = ' + age + ', gender = "' + gender + '", profile_bio = "' + bio + '", dietary_needs = "' + diet + '" WHERE username = "' + str(current_user)
                    print(sql)
                    
                    if request.form['password']:
                        password = str(request.form['password'])
                        passhash = str(hash_pass(password)).split("'")[1]
                        
                        sql = 'UPDATE user SET username = "' + username + '", password = "' + str(passhash) + '", height = ' + height + ', weight = ' + weight + ', age = ' + age + ', gender = "' + gender + '", profile_bio = "' + bio + '", dietary_needs = "' + diet + '" WHERE username = "' + str(current_user)

                    mycursor = mydb.cursor()
                    mycursor.execute(sql)
                    mydb.commit()
                    

                    selection = "*"
                    where = "username ='" + str(current_user) + "'"
                    data = queryingOn(method="SELECT", selection=selection,
                                    table_name="user", data=where)
                    result = "Profile updated successfully!"
                        
                else:
                    selection = "*"
                    where = "username ='" + str(current_user) + "'"
                    data = queryingOn(method="SELECT", selection=selection, table_name="user", data=where)
                    result = "Username exists"

                print(result)
                return render_template('home/profile.html', data=data)
    finally:
        mycursor.close()
        print("cur closed")


@blueprint.route('/pricechecker', methods=['GET'])
@login_required
def searchItem():
    print("Searching item...")
    try:
        if request.method == 'GET':
            input = str(request.args.get("search"))
            sql = "SELECT * FROM user WHERE username LIKE '%" + input + "%'"

            mycursor = mydb.cursor(buffered=True, dictionary=True)
            mycursor.execute(sql)
            mydb.commit()
            data = mycursor.fetchall()
            print("data", data)
            
            if data:
                return render_template('home/pricechecker.html', data=data)
            else:
                data = queryingOn(method="SELECT", selection="*", table_name="user")
                return render_template('home/pricechecker.html', data=data)
    finally:
        mycursor.close()
        print("cur closed")
    

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

@blueprint.route('/inventory.html')
def GetPantryItems():
    sql4= "SELECT id FROM user WHERE username= '" + str(current_user) + "'"
    mycursor4= mydb.cursor(buffered=True, dictionary=True)
    mycursor4.execute(sql4)
    uid= mycursor4.fetchall()
    sql = "SELECT p.uid, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.uid= (SELECT id FROM user WHERE username= '" + str(current_user) + "')"

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(sql)
    mydb.commit()
    pantry_items = mycursor.fetchall()
    print("data", pantry_items)
    sql2="SELECT SUM(weight) FROM pantry WHERE UID=(SELECT id FROM user WHERE username= '" + str(current_user) + "')"
    mycursor2 = mydb.cursor(buffered=True, dictionary=True)
    mycursor2.execute(sql2)
    pantryheaviest= mycursor2.fetchall()
    sql3="SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "'))"
    mycursor3 = mydb.cursor(buffered=True, dictionary=True)
    mycursor3.execute(sql3)
    fooditem= mycursor3.fetchall()
    #sql4="SELECT * FROM food_item e1 WHERE (SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND uid=1)"
    #mycursor4 = mydb.cursor(buffered=True, dictionary=True)
    #mycursor4.execute(sql4)
    #maxfoodname= mycursor3.fetchall()


    return render_template('home/inventory.html', pantry_items=pantry_items, pantryheaviest=pantryheaviest, fooditem=fooditem)

@blueprint.route('/updatepantry', methods = ['GET', 'POST'])
def update3():
        if request.method == "POST":
            weight = str(request.form['weight'])
            fid=str(request.form['fidsss'])
            sql="UPDATE pantry SET weight = '" + weight + "' WHERE uid = (SELECT id FROM user WHERE username= '" + str(current_user) + "') AND fid =" + str(fid)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            data = mycursor.fetchall()
            sql2 = "SELECT p.uid, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "')"

            mycursor2 = mydb.cursor(buffered=True, dictionary=True)
            mycursor2.execute(sql2)
            mydb.commit()
            pantry_items = mycursor2.fetchall()
            sql3="SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "'))"
            mycursor3 = mydb.cursor(buffered=True, dictionary=True)
            mycursor3.execute(sql3)
            mydb.commit()
            fooditem= mycursor3.fetchall()           
            return render_template("home/inventory.html",data=data, pantry_items=pantry_items, fooditem=fooditem)
            
@blueprint.route('/Createpantry', methods = ['GET', 'POST'])
def Create():
    if request.method == "POST":
        uid="1"
        weight = str(request.form['createweight'])
        fid=str(request.form['colours'])
        
        pantryitems = [
            (
                uid,
                fid,
                weight
            )
        ]
        sql= "INSERT INTO pantry (uid, fid, weight) VALUES ((SELECT id FROM user WHERE username= '" + str(current_user) + "'), '" + fid + "', '" + weight + "')"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        sql2 = "SELECT p.uid, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "')"

        mycursor2 = mydb.cursor(buffered=True, dictionary=True)
        mycursor2.execute(sql2)
        mydb.commit()
        pantry_items = mycursor2.fetchall()    
        sql3="SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "'))"
        mycursor3 = mydb.cursor(buffered=True, dictionary=True)
        mycursor3.execute(sql3)
        fooditem= mycursor3.fetchall()       
        return render_template("home/inventory.html",pantry_items=pantry_items, fooditem=fooditem)


@blueprint.route('/Removepantry', methods = ['GET', 'POST'])
def delete():
    if request.method == "POST":
        uid="1"
        fid=str(request.form['fidssr'])
        sql="DELETE FROM pantry WHERE uid = (SELECT id FROM user WHERE username= '" + str(current_user) + "') AND fid = '" + fid + "'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        mycursor2 = mydb.cursor(buffered=True, dictionary=True)
        sql2 = "SELECT p.uid, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "')"
        mycursor2.execute(sql2)
        mydb.commit()
        pantry_items = mycursor2.fetchall()  
        sql3="SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND uid=(SELECT id FROM user WHERE username= '" + str(current_user) + "'))"
        mycursor3 = mydb.cursor(buffered=True, dictionary=True)
        mycursor3.execute(sql3)
        fooditem= mycursor3.fetchall()           
        return render_template("home/inventory.html",pantry_items=pantry_items, fooditem=fooditem)

