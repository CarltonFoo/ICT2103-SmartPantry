from apps.home import mysqlbp, nosqlbp
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from Objects import sql_commands
from flask_login import (
    current_user,
    login_required
)
from Controls.queryControl import queryingMySQL, queryingNoSQL
from Objects.sql_commands import db
from apps.authentication.util import hash_pass
from apps.authentication.models import Users

from Objects.nosql_commands import NOSQL

nosql = NOSQL()

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


@mysqlbp.route('/index')
@login_required
def index():
    data = [("Data being pulled from MySQL database!"),
            ("MySQL is an open-source relational database management system.")]
    return render_template('home/index.html', segment='index', data=data)


@nosqlbp.route('/index')
@login_required
def index():
    data = [("Data being pulled from NoSQL database!"),
            ("MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.")]
    return render_template('home/index.html', segment='index', data=data)


@mysqlbp.route('/<template>')
@login_required
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'
        
        if template == "profile.html":
            data = queryingMySQL(method="SELECT", table_name='user', filterBy=['username'], filterVal=[str(current_user)])
            print(data)

        if template == "recipes.html":
            data = [("dummy data")]

        if template == "inventory.html":
            data = [("dummy data")]

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


@nosqlbp.route('/<template>')
@login_required
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        if template == "profile.html":
            data = queryingNoSQL(method="SELECT", collection='user', type="one", filterBy=['username'], filterVal=[str(current_user)])
            data = [data]

        if template == "recipes.html":
            data = [("dummy data")]

        if template == "inventory.html":
            data = [("dummy data")]

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


@mysqlbp.route('/updateprofile', methods=['GET', 'POST'])
@nosqlbp.route('/updateprofile', methods=['GET', 'POST'])
@login_required
def saveDetails():
    print("Updating profile...")
    if request.method == 'POST':
            
        userexist = Users.query.filter_by(username=request.form['username']).first()

        data = {
            "height": str(request.form['height']),
            "weight": str(request.form['weight']),
            "age": str(request.form['age']),
            "gender": str(request.form['gender']),
            "profile_bio": str(request.form['bio']),
            "dietary_needs": str(request.form['diet']),
        }
        
        if request.form['username'] == str(current_user):

            if request.form['password']:
                password = str(request.form['password'])
                passhash = str(hash_pass(password)).split("'")[1]

                data["password"] = passhash

            queryingMySQL(method="UPDATE", table_name="user", data=data, identifier="username", identifier_value=str(current_user))
            queryingNoSQL(method="UPDATE", collection="user", data=data, filterBy="username", filterVal=str(current_user), type="set")
            result = "Profile updated successfully!"
            
        elif not userexist:

            data["username"] = str(request.form['username'])

            if request.form['password']:
                password = str(request.form['password'])
                passhash = str(hash_pass(password)).split("'")[1]

                data["password"] = passhash
                
            queryingMySQL(method="UPDATE", table_name="user", data=data, identifier="username", identifier_value=str(current_user))
            queryingNoSQL(method="UPDATE", collection="user", data=data, filterBy="username", filterVal=str(current_user), type="set")
            result = "Profile updated successfully!"

            data = queryingMySQL(method="SELECT", table_name='user', filterBy=['username'], filterVal=[str(request.form['username'])])
            return render_template('home/profile.html', data=data)

        else:
            result = "Username exists"
    
        print(result)
        data = queryingMySQL(method="SELECT", table_name='user', filterBy=['username'], filterVal=[str(current_user)])
        return render_template('home/profile.html', data=data)


@mysqlbp.route('/pricechecker', methods=['GET'])
@login_required
def searchItem():
    print("Searching item...")
    try:
        if request.method == 'GET':
            input = str(request.args.get("search"))
            sql = "SELECT * FROM user WHERE username LIKE '%" + input + "%'"

            mycursor = db.cursor(buffered=True, dictionary=True)
            mycursor.execute(sql)
            db.commit()
            data = mycursor.fetchall()
            print("data", data)

            if data:
                return render_template('home/pricechecker.html', data=data)
            else:
                data = queryingMySQL(method="SELECT", selection="*", table_name="user")
                return render_template('home/pricechecker.html', data=data)
    finally:
        mycursor.close()
        print("cur closed")




@mysqlbp.route('/pricechecker.html')
def price_checker():
    food_items = queryingMySQL(method="SELECT", table_name='food_item')
    
    return render_template('home/pricechecker.html', food_items=food_items)


@nosqlbp.route('/pricechecker.html')
def price_checker():
    food_items = queryingNoSQL(method="SELECT", collection='food_item')

    return render_template('home/pricechecker.html', food_items=food_items)


@mysqlbp.route('/grocery_history', methods=['GET', 'POST'])
def grocery_history():
    if request.method == 'POST':
        user_id = current_user.id
        
        mycursor = db.cursor
        sql = "SELECT DISTINCT r.total_amount, month(ri.date) FROM receipt_ingredient ri, receipt r WHERE ri.receipt_id = r.receipt_id AND r.id = '{}'".format(user_id)
        
        mycursor.execute(sql)
        purchases = mycursor.fetchall()
        
        monthly_totals = {}
        for x, y in purchases:
            if y in monthly_totals:
                monthly_totals[y].append((x))
            else:
                monthly_totals[y] = [(x)]
            
        return jsonify({'purchases': monthly_totals})
    else:
        mycursor = db.cursor
        sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.id, r.total_amount FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.id = '{}' GROUP BY ri.receipt_id".format(current_user.id)

        mycursor.execute(sql)
        purchases = mycursor.fetchall()        
        
        food_list = []
        all_food_list = []
        for purchase in purchases:
            food_list = purchase[0].split(",")
            
            if (len(food_list) > 3):
                food_list[3] = "..."
                        
            all_food_list.append(", ".join(food_list[:4]))
            
        print(all_food_list)
        return render_template('home/history.html', purchases=purchases, all_food_list=all_food_list)


@mysqlbp.route('/get_purchase', methods=['POST'])
def get_purchase():
    if request.method == 'POST':
        receipt_id = request.form['receipt_id']

        sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.id, r.total_amount FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.id = '{}' AND r.receipt_id = '{}' GROUP BY ri.receipt_id".format(current_user.id, receipt_id)
        mycursor = db.cursor
        mycursor.execute(sql)
        purchases = mycursor.fetchall()

        details = {"food_items": [], "food_quantity": [], "original_weight": []}

        food_list = []
        price_list = []
        original_weight_list = []
        final_weight_list = []

        for purchase in purchases:
            food_list = purchase[0].split(",")
            price_list = purchase[1].split(",")
            original_weight_list = purchase[2].split(",")
            final_weight_list = purchase[4].split(",")

        price_list = list(map(float, price_list))

        original_weight_list = list(map(float, original_weight_list))
        final_weight_list = list(map(float, final_weight_list))

        quantity_list = []
        quantity = 0

        for i in range(len(original_weight_list)):
            quantity = final_weight_list[i] / original_weight_list[i]
            quantity_list.append(int(quantity))

        # total_amt = 0
        # for i in range(len(price_list)):
        #     total_amt += price_list[i] * quantity_list[i]

        # total_amt = "{:.2f}".format(total_amt)

        details["food_items"] = food_list
        details["food_quantity"] = quantity_list
        details["original_weight"] = original_weight_list

        print(details)

        return render_template('home/purchase_detail.html', purchases=purchases, details=details)


@mysqlbp.route('/insert_receipt', methods=["POST"])
def insert_receipt():
    if request.method == 'POST':
        total_amt = request.form['total_amt']
        
        receipt = [
            (
                current_user.id,
                total_amt
            )
        ]

        db.insert_data(table_name="receipt", table_columns=["id, total_amount"], values=receipt)

        mycursor = db.cursor
        mycursor.execute("SELECT receipt_id FROM receipt ORDER BY receipt_id DESC LIMIT 1")
        receipt_id = mycursor.fetchone()

        return jsonify({'receipt_id': receipt_id})


@mysqlbp.route('/insert_receipt_ingredient', methods=["POST"])
def insert_receipt_ingredient():
    if request.method == 'POST':
        receipt_id = request.form['receipt_id']
        fid = request.form['fid']
        weight = request.form['weight']
        date = request.form['date']

        receipt_ingredient = [
            (
                receipt_id,
                fid,
                weight,
                date
            )
        ]
        db.insert_data(table_name="receipt_ingredient", table_columns=["receipt_id", "fid", "weight", "date"], values=receipt_ingredient)

        return jsonify({'response': "OK"})
    
    
@mysqlbp.route('/inventory.html')
def GetPantryItems():
    sql4 = "SELECT id FROM user WHERE username= '" + str(current_user) + "'"
    mycursor4 = db.cursor(buffered=True, dictionary=True)
    mycursor4.execute(sql4)
    id = mycursor4.fetchall()
    sql = "SELECT p.id, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.id= (SELECT id FROM user WHERE username= '" + str(
        current_user) + "')"

    mycursor = db.cursor(buffered=True, dictionary=True)
    mycursor.execute(sql)
    db.commit()
    pantry_items = mycursor.fetchall()
    print("data", pantry_items)
    sql2 = "SELECT SUM(weight) FROM pantry WHERE id=(SELECT id FROM user WHERE username= '" + \
        str(current_user) + "')"
    mycursor2 = db.cursor(buffered=True, dictionary=True)
    mycursor2.execute(sql2)
    pantryheaviest = mycursor2.fetchall()
    sql3 = "SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND id=(SELECT id FROM user WHERE username= '" + str(
        current_user) + "'))"
    mycursor3 = db.cursor(buffered=True, dictionary=True)
    mycursor3.execute(sql3)
    fooditem = mycursor3.fetchall()
    #sql4="SELECT * FROM food_item e1 WHERE (SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND id=1)"
    #mycursor4 = db.cursor(buffered=True, dictionary=True)
    #mycursor4.execute(sql4)
    #maxfoodname= mycursor3.fetchall()

    return render_template('home/inventory.html', pantry_items=pantry_items, pantryheaviest=pantryheaviest, fooditem=fooditem)


@mysqlbp.route('/updatepantry', methods=['GET', 'POST'])
def update3():
    if request.method == "POST":
        weight = str(request.form['weight'])
        fid = str(request.form['fidsss'])
        sql = "UPDATE pantry SET weight = '" + weight + \
            "' WHERE id = (SELECT id FROM user WHERE username= '" + \
            str(current_user) + "') AND fid =" + str(fid)
        mycursor = db.cursor()
        mycursor.execute(sql)
        db.commit()
        data = mycursor.fetchall()
        sql2 = "SELECT p.id, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "')"

        mycursor2 = db.cursor(buffered=True, dictionary=True)
        mycursor2.execute(sql2)
        db.commit()
        pantry_items = mycursor2.fetchall()
        sql3 = "SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "'))"
        mycursor3 = db.cursor(buffered=True, dictionary=True)
        mycursor3.execute(sql3)
        db.commit()
        fooditem = mycursor3.fetchall()
        return render_template("home/inventory.html", data=data, pantry_items=pantry_items, fooditem=fooditem)

    
@mysqlbp.route('/Createpantry', methods=['GET', 'POST'])
def Create():
    if request.method == "POST":
        id = "1"
        weight = str(request.form['createweight'])
        fid = str(request.form['colours'])

        pantryitems = [
            (
                id,
                fid,
                weight
            )
        ]
        sql = "INSERT INTO pantry (id, fid, weight) VALUES ((SELECT id FROM user WHERE username= '" + \
            str(current_user) + "'), '" + fid + "', '" + weight + "')"
        mycursor = db.cursor()
        mycursor.execute(sql)
        db.commit()
        sql2 = "SELECT p.id, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "')"

        mycursor2 = db.cursor(buffered=True, dictionary=True)
        mycursor2.execute(sql2)
        db.commit()
        pantry_items = mycursor2.fetchall()
        sql3 = "SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "'))"
        mycursor3 = db.cursor(buffered=True, dictionary=True)
        mycursor3.execute(sql3)
        fooditem = mycursor3.fetchall()
        return render_template("home/inventory.html", pantry_items=pantry_items, fooditem=fooditem)


@mysqlbp.route('/Removepantry', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        id = "1"
        fid = str(request.form['fidssr'])
        sql = "DELETE FROM pantry WHERE id = (SELECT id FROM user WHERE username= '" + str(
            current_user) + "') AND fid = '" + fid + "'"
        mycursor = db.cursor()
        mycursor.execute(sql)
        db.commit()
        mycursor2 = db.cursor(buffered=True, dictionary=True)
        sql2 = "SELECT p.id, p.fid, p.weight, e.food_name FROM food_item e, pantry p WHERE e.fid = p.fid AND p.id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "')"
        mycursor2.execute(sql2)
        db.commit()
        pantry_items = mycursor2.fetchall()
        sql3 = "SELECT * FROM food_item e1 WHERE NOT EXISTS( SELECT * FROM pantry AS e2 WHERE e1.fid = e2.fid AND id=(SELECT id FROM user WHERE username= '" + str(
            current_user) + "'))"
        mycursor3 = db.cursor(buffered=True, dictionary=True)
        mycursor3.execute(sql3)
        fooditem = mycursor3.fetchall()
        return render_template("home/inventory.html", pantry_items=pantry_items, fooditem=fooditem)
