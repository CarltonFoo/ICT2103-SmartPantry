from flask import Blueprint, request
from flask.json import jsonify
from flask.wrappers import Response
import json
from ..extensions import mongo

foodNOSQL = Blueprint('foodNOSQL',__name__)

# get all food
@foodNOSQL.route('/food',methods=['GET'])
def get_all_food():
    try:
        food_collection = mongo.db.food_items
        food_list = list(food_collection.find())
        for food in food_list:
            food["_id"] = str(food["_id"])
        return jsonify(food_list)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
    )
