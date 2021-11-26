from Objects.sql_commands import *
from Objects.nosql_commands import *

def queryingOn(data=None, table_name: str = None, method: str = "SELECT", getheaders: list = None, filterBy: list = None, filterVal: list = None, identifier: str = None, identifier_value: str = None, type: str = None, collection: str = None, field=None):
    
    nosql = NOSQL();
    
    if data is None and table_name is None:
        return
    elif data is None:
        pass

    if method == "SELECT":
        #mySQL
        sql_result = select_data(table_name=table_name, getheaders=getheaders, filterBy= filterBy, filterVal= filterVal)
        #noSQL
        nosql_result = nosql.select_data(type=type, collection=collection, filterBy=filterBy, filterVal=filterVal)
        return sql_result, nosql_result

    if method == "INSERT":
        # mySQL
        sql_result = insert_data(table_name=table_name, table_columns=data.keys(), values=data.values())
        # noSQL
        nosql_result = nosql.insert_data(collection=collection, data=data)
        return sql_result, nosql_result
        
    elif method == "DELETE":
        # mySQL
        sql_result = delete_data(table_name=table_name, identifier_value=identifier_value, identifier=identifier)
        # noSQL
        nosql_result = nosql.delete_data(collection=collection, data=data, type=type)
        return sql_result, nosql_result

    elif method == "UPDATE":
        # mySQL
        sql_result = update_data(table_name=table_name, data=data, identifier_value=identifier_value, identifier=identifier)
        # noSQL
        nosql_result = nosql.update_data(collection=collection, data=data, filterBy=filterBy, filterVal=filterVal, type=type, field=field)
        return sql_result, nosql_result
