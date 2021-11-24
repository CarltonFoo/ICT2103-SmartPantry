from pymongo import MongoClient
import ssl
client = MongoClient("mongodb+srv://ict2103:2103isgreat@cluster0.xszjw.mongodb.net/?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
mongo = client.get_database("SmartPantry")