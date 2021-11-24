from dns import exception
from flask import Blueprint, request
from flask.json import jsonify
from flask.wrappers import Response
import json
from ..extensions import mongo

usersNOSQL = Blueprint('usersNOSQL',__name__)

user = {
    "id":"x",
    "user_name":"hi",
    "password":"hashed",
    "gender":"M",
    "height(cm)": 170,
    "profile_bio": "",
    "dietary_needs": "",
    "age":32,
    "pantry": [
    {
      "food_name":"Small Prawns",
      "measurement(g)":1000
    },
    {
      "food_name":"Whole Chicken",
      "measurement(g)":2000
    }
    ,{
      "food_name":"Coconut Milk",
      "measurement(g)": 50
    }
  ]
}
@usersNOSQL.route('/users',methods=['GET'])
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
@usersNOSQL.route("/users/<username>",methods=['GET'])
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
@usersNOSQL.route("/users/<username>",methods=['PATCH'])
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
# update the pantry list
@usersNOSQL.route("/users/pantry/<username>",methods=['PATCH'])
def update_pantry():
    pass
