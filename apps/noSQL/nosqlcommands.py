from dns import exception
from flask import Blueprint, request
from flask.json import jsonify
from flask.wrappers import Response
import json
from ..extensions import mongo

''' FOOD COLLECCTION'''
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
# retrieve food document 
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
'''Recipe Collection Queries'''
# get all recipe document in db
def get_all_recipes():
    try:
        recipe_collection = mongo.Recipe
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
# get recipe document by name
def get_recipe(name):
    try:
        recipe_collection = mongo.Recipe
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
# get all recipe under specified calories
def get_recipe_under_calories(calories):
    try:
        recipe_collection = mongo.Recipe
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
'''users commands'''
def get_users():
    try:
        users = mongo.user
        user_list = list(users.find())
        for user in user_list:
            user["_id"] = str(user["_id"])
        return jsonify(user_list)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
)
# Retrieve user document
def get_user(username):
    try:
        user_collection = mongo.user 
        user = user_collection.find_one({"username":username})
        user["_id"] = str(user["_id"])
        return jsonify(user)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
        )
# Update user info
def update_user(username):
    try:
        user_collection = mongo.user 
        user_collection.update_one(
            {'username':username},
            {
                "$set":{
                "gender": request.form['gender'],
                "age": request.form['age'],
                "height": request.form['height'],
                "weight": request.form['weight'],
                "dietary_needs": request.form['dietary_needs']
            }
            }
        )
        return Response(    
                response=json.dumps({"message":"user updated"}),
                status=200,
                mimetype="application/json"
            ) 
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
        )
    
# Insert food item into the user's pantry
def insert_pantry(username,food_item):
    try:
        user_collection = mongo.user
     
        user_collection.update_one(
            {'username':username},
            {
                "$push":{
                    "pantry": food_item
                }
            }
        )
        return Response(    
                response=json.dumps({"message":"user updated"}),
                status=200,
                mimetype="application/json"
            ) 
    except exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"cannot read Recipe"}),
            status=500,
            mimetype="application/json"
        )

