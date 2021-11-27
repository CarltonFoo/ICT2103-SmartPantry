from Model import user
from Objects import sql_commands


def queryingOn(method: str = "SELECT", selection=None, table_name: str = None, data=None):
    if data is None and table_name is None:
        return
    elif data is None:
        pass

    if method == "SELECT":
        #mySQL
        # sql_result = select_columns(selection=selection, table_name=table_name, where=data)
        #noSQL
        nosql_result = None
        
        # return sql_result

    # Instantiate object
    if table_name == "USERS":
        instance = User(data)

    if method == "INSERT":
        # mySQL
        # insert_data(table_name=table_name, data=instance.getter())
        # noSQL
        
        pass
    elif method == "DELETE":
        # delete_data(table_name=table_name, identifier_value=instance.getID())
        pass
    elif method == "UPDATE":
        pass

    pass
