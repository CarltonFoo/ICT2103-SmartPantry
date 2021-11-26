from Objects.sql_commands import *

def queryingOn(data=None, table_name:str=None, method:str = "SELECT", getheaders: list = None, filterBy: list = None, filterVal: list = None, identifier: str = None, identifier_value: str = None):
    if data is None and table_name is None:
        return
    elif data is None:
        pass

    if method == "SELECT":
        #mySQL
        sql_result = select_data(table_name=table_name,getheaders= getheaders, filterBy= filterBy, filterVal= filterVal)
        #noSQL
        nosql_result = None
        return sql_result, nosql_result

    if method == "INSERT":
        # mySQL
        insert_data(table_name=table_name, table_columns= data.keys(), values = data.values())
        # noSQL
        
    elif method == "DELETE":
        delete_data(table_name=table_name, identifier_value=identifier_value, identifier=identifier)

    elif method == "UPDATE":
        # mySQL
        update_data(table_name=table_name, data=data,identifier_value=identifier_value, identifier=identifier)
