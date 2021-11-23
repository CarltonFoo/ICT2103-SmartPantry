from apps.home import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from Objects import sql_commands
from flask_login import (
    current_user
)

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

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


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
    food_items = sql_commands.select_columns("food_item", "*")

    return render_template('home/pricechecker.html', food_items=food_items)


@blueprint.route('/grocery_history')
def grocery_history():
    mycursor = sql_commands.mydb.cursor()
    sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.uid FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.uid = '{}' GROUP BY ri.receipt_id".format(current_user.id)

    mycursor.execute(sql)
    purchases = mycursor.fetchall()

    return render_template('home/history.html', purchases=purchases)


@blueprint.route('/get_purchase', methods=['POST'])
def get_purchase():
    if request.method == 'POST':
        receipt_id = request.form['receipt_id']

        sql = "SELECT GROUP_CONCAT(fi.food_name), GROUP_CONCAT(fi.price), GROUP_CONCAT(fi.weight), ri.receipt_id, GROUP_CONCAT(ri.weight), ri.date, r.uid FROM food_item fi, receipt_ingredient ri, receipt r WHERE fi.fid = ri.fid AND r.receipt_id = ri.receipt_id AND r.uid = '{}' AND r.receipt_id = '{}' GROUP BY ri.receipt_id".format(current_user.id, receipt_id)
        mycursor = sql_commands.mydb.cursor()
        mycursor.execute(sql)
        purchases = mycursor.fetchall()

        details = {"food_items": [],
                   "food_quantity": [], "original_weight": []}

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

        total_amt = 0
        for i in range(len(price_list)):
            total_amt += price_list[i] * quantity_list[i]

        total_amt = "{:.2f}".format(total_amt)

        details["food_items"] = food_list
        details["food_quantity"] = quantity_list
        details["original_weight"] = original_weight_list

        print(details)

        return render_template('home/purchase_detail.html', purchases=purchases, details=details, total_amt=total_amt)


@blueprint.route('/insert_receipt', methods=["POST"])
def insert_receipt():
    if request.method == 'POST':
        receipt = {
            "uid": current_user.id
        }

        sql_commands.insert_data("receipt", receipt)

        mycursor = sql_commands.mydb.cursor()
        mycursor.execute(
            "SELECT receipt_id FROM receipt ORDER BY receipt_id DESC LIMIT 1")
        receipt_id = mycursor.fetchone()

        return jsonify({'receipt_id': receipt_id})


@blueprint.route('/insert_receipt_ingredient', methods=["POST"])
def insert_receipt_ingredient():
    if request.method == 'POST':
        receipt_id = request.form['receipt_id']
        fid = request.form['fid']
        weight = request.form['weight']
        date = request.form['date']

        receipt_ingredient = {
            "receipt_id": receipt_id,
            "fid": fid,
            "weight": weight,
            "date": date
        }
        sql_commands.insert_data("receipt_ingredient", receipt_ingredient)

        return jsonify({'response': "OK"})
