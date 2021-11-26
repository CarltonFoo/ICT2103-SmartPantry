from apps.home import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from Objects import sql_commands
from flask_login import (
    current_user,
    login_required
)
from Controls.queryControl import queryingOn
from Objects.sql_commands import db
from apps.authentication.util import hash_pass
from apps.authentication.models import Users


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'
        
        if template == "profile.html":
            data = queryingOn(method="SELECT", table_name="user", filterBy=['username'], filterVal=[str(current_user)])[0]

        if template == "recipes.html":
            data = [("dummy data")]

        if template == "inventory.html":
            data = [("dummy data")]

        if template == "pricechecker.html":
            data = queryingOn(method="SELECT", table_name="user")

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

                    sql = 'UPDATE user SET username = "' + username + '", height = ' + height + ', weight = ' + weight + ', age = ' + age + \
                        ', gender = "' + gender + '", profile_bio = "' + bio + \
                        '", dietary_needs = "' + diet + \
                        '" WHERE username = "' + str(current_user)
                    print(sql)

                    if request.form['password']:
                        password = str(request.form['password'])
                        passhash = str(hash_pass(password)).split("'")[1]

                        sql = 'UPDATE user SET username = "' + username + '", password = "' + \
                            str(passhash) + '", height = ' + height + ', weight = ' + weight + ', age = ' + age + ', gender = "' + gender + \
                            '", profile_bio = "' + bio + '", dietary_needs = "' + \
                            diet + '" WHERE username = "' + str(current_user)

                    mycursor = db.cursor()
                    mycursor.execute(sql)
                    db.commit()

                    selection = "*"
                    where = "username ='" + str(current_user) + "'"
                    data = queryingOn(method="SELECT", selection=selection, table_name="user", data=where)
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

            mycursor = db.cursor(buffered=True, dictionary=True)
            mycursor.execute(sql)
            db.commit()
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


@blueprint.route('/price_checker')
def price_checker():
    food_items = db.select_data(table_name="food_item")

    return render_template('home/pricechecker.html', food_items=food_items)


@blueprint.route('/grocery_history', methods=['GET', 'POST'])
def grocery_history():
    if request.method == 'POST':
        user_id = current_user.id
        
        mycursor = db.cursor
        sql = "SELECT DISTINCT r.total_amount, month(ri.date) FROM receipt_ingredient ri, receipt r WHERE ri.receipt_id = r.receipt_id AND r.uid = '{}'".format(user_id)
        
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
        sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.uid, r.total_amount FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.uid = '{}' GROUP BY ri.receipt_id".format(current_user.id)

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


@blueprint.route('/get_purchase', methods=['POST'])
def get_purchase():
    if request.method == 'POST':
        receipt_id = request.form['receipt_id']

        sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.uid, r.total_amount FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.uid = '{}' AND r.receipt_id = '{}' GROUP BY ri.receipt_id".format(current_user.id, receipt_id)
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


@blueprint.route('/insert_receipt', methods=["POST"])
def insert_receipt():
    if request.method == 'POST':
        total_amt = request.form['total_amt']
        
        receipt = [
            (
                current_user.id,
                total_amt
            )
        ]

        db.insert_data(table_name="receipt", table_columns=["uid, total_amount"], values=receipt)

        mycursor = db.cursor
        mycursor.execute("SELECT receipt_id FROM receipt ORDER BY receipt_id DESC LIMIT 1")
        receipt_id = mycursor.fetchone()

        return jsonify({'receipt_id': receipt_id})


@blueprint.route('/insert_receipt_ingredient', methods=["POST"])
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
