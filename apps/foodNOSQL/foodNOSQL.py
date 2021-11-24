from dns import exception
from flask import Blueprint, request
from flask.json import jsonify
from flask.wrappers import Response
import json
from ..extensions import mongo

foodNOSQL = Blueprint('foodNOSQL',__name__)

# get all food items 
@foodNOSQL.route('/food',methods=['GET'])
def get_all_food():
    try:
        food_collection = mongo.food_item
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

# Retrieve a single food doc
@foodNOSQL.route('/food/<name>',methods=['GET'])
def get_food(name):
    try:
        food_collection = mongo.food_item
        food = food_collection.find_one({'name':name})
        food["_id"] = str(food["_id"])
        return jsonify(food)
    except exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot find Recipe"}),
            status=500,
            mimetype="application/json"
        )
# Food item search by name
@foodNOSQL.route('/food/search/<name>',methods=['GET'])
def search_food(name):
    try:
        food_collection = mongo.food_item
        food_list = list(food_collection.find({'name':{'$regex': name, '$options':'i'}}))
        for food in food_list:
            food["_id"] = str(food["_id"])
        return jsonify(food_list)
    except exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot find Recipe"}),
            status=500,
            mimetype="application/json"
        )
