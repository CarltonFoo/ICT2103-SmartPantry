from os import environ
from os.path import join, dirname
from pymongo import MongoClient
from dotenv import load_dotenv
import ssl

dotenv_path = join(dirname(__file__), '../', '.env')
load_dotenv(dotenv_path)


NOSQL_USERNAME = environ.get("NOSQL_USERNAME")
NOSQL_PASSWORD = environ.get("NOSQL_PASSWORD")
NOSQL_DATABASE = environ.get("NOSQL_DATABASE")


class NOSQL:
    def __init__(self) -> None:
        self.client = MongoClient(f"mongodb+srv://{NOSQL_USERNAME}:{NOSQL_PASSWORD}@cluster0.xszjw.mongodb.net/?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.client.get_database(NOSQL_DATABASE)

    def insert_data(self, collection: str = "user", data=None):
        dataLength = len(data[0])
        if dataLength > 1:
            return self.db[collection].insert_many(data)
        elif dataLength == 1:
            return self.db[collection].insert_one(data[0])            
        else:
            raise ValueError('Missing data')

    def delete_data(self, collection: str = "user", data=None, type="one"):
        if data is None:
            raise ValueError('Missing data')
        elif data == {} or type == "many":
            return self.db[collection].delete_many(data)
        elif type == "one":
            return self.db[collection].delete_one(data)

    def select_data(self, type='all', collection: str = None, filterBy=None, filterVal=None):
        if collection is None:
            raise ValueError("Missing parameter Collection")

        if filterBy is None or filterVal is None or type == "all":
            return list(self.db[collection].find())
        elif type == 'one':
            return self.db[collection].find_one({filterBy[0]: filterVal[0]})

    def update_data(self, collection: str = None, data=None, filterBy=None, filterVal=None, type="set", field=None):
        if field is None and type == 'set':
            self.db[collection].update_one(
                {filterBy: filterVal},
                {
                    f"${type}": data
                }
            )
        elif type == 'push' or type == 'pull':
            self.db[collection].update_one(
                {filterBy: filterVal},
                {
                    f"${type}": {
                        field: data
                    }
                }
            )