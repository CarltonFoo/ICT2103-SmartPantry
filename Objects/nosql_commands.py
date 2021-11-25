from os import environ
from os.path import join, dirname
from pymongo import MongoClient
from flask import jsonify
from dotenv import load_dotenv
import ssl

dotenv_path = join(dirname(__file__), '../','.env')
load_dotenv(dotenv_path)


NOSQL_USERNAME = environ.get("NOSQL_USERNAME")
NOSQL_PASSWORD = environ.get("NOSQL_PASSWORD")
NOSQL_DATABASE = environ.get("NOSQL_DATABASE")




class NOSQL:
    def __init__(self) -> None:
        self.client = MongoClient(f"mongodb+srv://{NOSQL_USERNAME}:{NOSQL_PASSWORD}@cluster0.xszjw.mongodb.net/?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.client.get_database(NOSQL_DATABASE)

    def insert_data(self, collection:str = "user", data = None):
        dataLength = len(data)
        if dataLength > 1:
            return self.db[collection].insert_many(data)
        elif dataLength == 1:
            return self.db[collection].insert_one(data)
        else:
            raise ValueError('Missing data')

    def delete_data(self, collection:str = "user", data = None, type="many"):
        if data is None:
            raise ValueError('Missing data')
        elif data == {} or type=="many":
            return self.db[collection].delete_many(data)
        elif type == "one":
            return self.db[collection].delete_one(data)


# userData = [
# {
#         "username": "Hello11",
#         "gender" : "F",
#         'age': "40",
#         'height': "1000",
#         "weight": "3000",
#         "dietary_needs": "Seafood",
#         "pantry": [],
#     },
#     {
#         "username": "oasdad7",
#         "gender" : "F",
#         'age': "40",
#         'height': "1000",
#         "weight": "3000",
#         "dietary_needs": "Seafood",
#         "pantry": [],

#     }

# ]

# userDataDelete = {
#         "username": {"$regex":"/^hello.*/"}
#     }




# userDataDelete = {}

# db = NOSQL()
# result = db.insert_data(data=userData)

# result = db.delete_data(data=userDataDelete)
# print(result)