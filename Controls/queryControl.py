import Objects.sql_commands
from Model.user import User
from Objects.sql_commands import delete_data, insert_data, select_all_columns


def queryingOn(data=None, table_name:str=None,method:str = "SELECT"):
    if data is None and table_name is None:
        return
    elif data is None:
        pass

    if method == "SELECT":
        #mySQL
        sql_result = select_all_columns(table_name=table_name)
        #noSQL
        nosql_result = None
        
        return sql_result

    # Instantiate object
    if table_name == "USERS":
        instance = User(data)

    if method == "INSERT":
        # mySQL
        insert_data(table_name=table_name, data=instance.getter())
        # noSQL
        
        pass
    elif method == "DELETE":
        delete_data(table_name=table_name, identifier_value=instance.getID())
        pass
    elif method == "UPDATE":
        pass

    pass


def _select():
    pass

def _insert():
    pass

def _delete():
    pass

def _update():
    pass