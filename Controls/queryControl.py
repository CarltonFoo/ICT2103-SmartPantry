from Objects.sql_commands import *
from Objects.nosql_commands import *
from mysql.connector import errorcode, Error

def queryingMySQL(data=None, table_name: str = None, method: str = "SELECT", getheaders: list = None, filterBy: list = None, filterVal: list = None, identifier: str = None, identifier_value: str = None):

    if method == "SELECT":
        try:
            #mySQL
            sql_result = select_data(table_name=table_name, getheaders=getheaders, filterBy=filterBy, filterVal=filterVal)
            return sql_result
        except Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                print(f'Create table {table_name}')
                dir = os.path.join(os.path.dirname(__file__), "../Objects/sql_scripts/", f'{table_name}.sql')
                create_table(table_name=table_name, dir=dir)
                sql_result = select_data(table_name=table_name, getheaders=getheaders, filterBy=filterBy, filterVal=filterVal)
                return sql_result

    if method == "INSERT":
        # mySQL

        try:
            #mySQL
            sql_result = insert_data(table_name=table_name, table_columns=data.keys(), values=data.values())
            return sql_result
        except Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                print(f'Create table {table_name}')
                dir = os.path.join(os.path.dirname(__file__), "../Objects/sql_scripts/", f'{table_name}.sql')
                create_table(table_name=table_name, dir=dir)
                sql_result = insert_data(table_name=table_name, table_columns=data.keys(), values=data.values())
                return sql_result

    elif method == "DELETE":
        try:
            #mySQL
            sql_result = delete_data(table_name=table_name, identifier_value=identifier_value, identifier=identifier)
            return sql_result
        except Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                print(f'Create table {table_name}')
                dir = os.path.join(os.path.dirname(__file__), "./sql_scripts/", f'{table_name}.sql')
                create_table(table_name=table_name, dir=dir)
                sql_result = delete_data(table_name=table_name, identifier_value=identifier_value, identifier=identifier)
                return sql_result


    elif method == "UPDATE":
        try:
            #mySQL
            sql_result = update_data(table_name=table_name, data=data, identifier_value=identifier_value, identifier=identifier)
            return sql_result
        except Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                print(f'Create table {table_name}')
                dir = os.path.join(os.path.dirname(__file__), "./sql_scripts/", f'{table_name}.sql')
                create_table(table_name=table_name, dir=dir)
                sql_result = update_data(table_name=table_name, data=data, identifier_value=identifier_value, identifier=identifier)
                return sql_result



def queryingNoSQL(data=None, method: str = "SELECT", filterBy: list = None, filterVal: list = None, type: str = None, collection: str = None, field=None):

    nosql = NOSQL()

    if method == "SELECT":
        #noSQL
        nosql_result = nosql.select_data(type=type, collection=collection, filterBy=filterBy, filterVal=filterVal)
        return nosql_result

    if method == "INSERT":
        # noSQL
        nosql_result = nosql.insert_data(collection=collection, data=data)
        return nosql_result

    elif method == "DELETE":
        # noSQL
        nosql_result = nosql.delete_data(collection=collection, data=data, type=type)
        return nosql_result

    elif method == "UPDATE":
        # noSQL
        nosql_result = nosql.update_data(collection=collection, data=data, filterBy=filterBy, filterVal=filterVal, type=type, field=field)
        return nosql_result
