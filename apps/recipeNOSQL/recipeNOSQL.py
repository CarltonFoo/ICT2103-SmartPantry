import re
from flask import Blueprint, request
from flask.json import jsonify
from flask.wrappers import Response
import json
from ..extensions import mongo

recipeNOSQL = Blueprint('recipeNOSQL',__name__)
# get all recipes
@recipeNOSQL.route('/recipe',methods=['GET'])
def get_all_recipes():
    try:
        recipe_collection = mongo.db.Recipe
        recipe_list = list(recipe_collection.find())
        for recipe in recipe_list:
            recipe["_id"] = str(recipe["_id"])
        return jsonify(recipe_list)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
        )
# get recipe name
@recipeNOSQL.route('/recipe/<name>',methods=['GET'])
def get_recipe(name):
    try:
        recipe_collection = mongo.db.Recipe
        recipe = recipe_collection.find_one({'recipe_name':name})
        recipe["_id"] = str(recipe["_id"])
        return jsonify(recipe)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot find Recipe"}),
            status=500,
            mimetype="application/json"
        )
'''
will figure out how to do this later
@recipeNOSQL.route('/recipe',methods=['POST'])
def insert_recipe():
    try:
        recipe = {
            "recipe_name":request.form["name"],
            "ingredients":{
                "food_name":request.form["food_name"],
                "measurement(g)":int(request.form["measurement"])
            },
            "Calories":int(request.form["calories"]),
            "Dietary Types":request.form["diet_type"],
            "Marinates and Side Ingredients":request.form["side"],
            "Steps":request.form["steps"]
        }
        dbResponse = mongo.db.Recipe.insert_one(recipe)
        return Response(    
            response=json.dumps({"message":"user created", "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot insert"}),
            status=500,
            mimetype="application/json"
        )
'''
# get all recipe under specified calories
@recipeNOSQL.route('/recipe/calories/<calories>')
def get_recipe_under_calories(calories):
    try:
        recipe_collection = mongo.db.Recipe
        recipe_list = list(recipe_collection.find({'Calories':{'$lte':int(calories)}}))
        for recipe in recipe_list:
            recipe["_id"] = str(recipe["_id"])
        return jsonify(recipe_list)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"No such recipe"}),
            status=500,
            mimetype="application/json"
        )

# 