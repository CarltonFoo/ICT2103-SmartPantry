import mysql.connector

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../', '.env')
load_dotenv(dotenv_path)

SQL_USERNAME = os.environ.get("SQL_USERNAME")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_DATABASE = os.environ.get("SQL_DATABASE")

db = mysql.connector.connect(
    host="localhost",
    user=SQL_USERNAME,
    password=SQL_PASSWORD,
    database=SQL_DATABASE
)

cursor = db.cursor(buffered=True, dictionary=True)
cursor2 = db.cursor()

def listToStr(listOfData):
    """Convert list to a string with coma separated"""
    return ",".join(listOfData)


def concatList(list1: list = None, list2: list = None, char: str = "="):
    combine = zip(list1, list2)
    result = []
    for ele1, ele2 in combine:
        result.append( ele1 + char + "'" + ele2 + "'")
    return result[0]

# class __Query:
#     def __init__(self) -> None:
#         self.db = mysql.connector.connect(
#             host="localhost",
#             user=SQL_USERNAME,
#             password=SQL_PASSWORD,
#             database=SQL_DATABASE
#         )
#         self.cursor = self.db.cursor()

#     @abstractclassmethod
#     def remove(self):
#         pass
#     @abstractclassmethod
#     def new(self):
#         pass
#     @abstractclassmethod
#     def modify(self):
#         pass
#     pass


# class TableQuery(__Query):
#     def new(self, table_name:str, ifExists:str = 'NOT EXISTS', ):
#         self.cursor.execute(f'CREATE TABLE IF {ifExists.upper()} {table_name}')
#     pass

# class DataQuery(__Query):
#     pass

# SQL Database connection
# class SQL_Database(TableQuery, DataQuery):

# class SQL_Database:
#     """Class represents sql dataabase, and contains attributes and methods pertaining to SQL"""

# def __init__(self) -> None:
#     # __Query.__init__()
#     self.db = mysql.connector.connect(
#         host="localhost",
#         user=SQL_USERNAME,
#         password=SQL_PASSWORD,
#         database=SQL_DATABASE
#     )
#     self.cursor = self.db.cursor()

def select_data(getheaders: list = None, filterBy: list = None, filterVal: list = None, table_name: str = None):
    """SQL Query data based on 3 inputs headers, values and table name.

    headers: Type of list. Header name
    col_values: Type of list. Values corresponding to given headers
    table_name: Type of str. String representation of table
    ."""
    if table_name is None or table_name.isspace():
        raise ValueError(
            "Table name cannot be Null value or whitespace characters")
    
    if getheaders is None and filterBy is None and filterVal is None:
        cursor.execute(f"SELECT * from {table_name}")
    else:
        if len(filterBy) != len(filterVal):
            raise ValueError(
                "Lists of filterBy and filterVal have different length")

        if filterBy is None:
            cols = listToStr(getheaders)
            cursor.execute(f"SELECT {cols} from {table_name}")
        elif getheaders is None:
            where = concatList(filterBy, filterVal)
            cursor.execute(f"SELECT * from {table_name} WHERE {where}")

    result = cursor.fetchall()
    return result

def insert_data(table_name: str = None, table_columns: list = None, values: list = None):
    columns_string = listToStr(table_columns)
    values_string = ', '.join(f"{w}" for w in values)

    if "," not in values_string:
        sql = "INSERT INTO " + table_name + " (" + columns_string + ") VALUES(" + values_string + ")"
    else:
        sql = "INSERT INTO " + table_name + " (" + columns_string + ") VALUES" + values_string
        
    cursor.execute(sql)
    db.commit()

    print(f"data inserted to {table_name} table successfully.")

def delete_data(table_name: str, identifier: str = None, identifier_value: str = None):
    if table_name is None or table_name.isspace():
        raise ValueError(
            "Table name cannot be Null value or whitespace characters")

    if identifier is None and identifier_value is None:
        cursor.execute(f"DELETE FROM {table_name}")
        db.commit()

        print(f"{table_name} table deleted successfully.")
    else:
        cursor.execute(
            f'DELETE FROM {table_name} WHERE {identifier}="{identifier_value}"')
        db.commit()

        print(f"data deleted from {table_name} table successfully.")

def update_data(table_name: str, data: dict, identifier: str, identifier_value: str):
    if table_name is None or table_name.isspace():
        raise ValueError(
            "Table name cannot be Null value or whitespace characters")

    if data is not None:
        for key, value in data.items():
            sql = ""

            if type(value) == str:
                sql = f'UPDATE {table_name} SET `{key}`="{value}" WHERE {identifier}="{identifier_value}"'
            else:
                sql = f'UPDATE {table_name} SET `{key}`={value} WHERE {identifier}="{identifier_value}"'

            cursor.execute(sql)

        db.commit()
        print(f"{table_name} table updated successfully.")


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ict2103project_database"
# )

# Things to do: create functions for the following SQL statements
# SELECT /
# UPDATE /
# DELETE /
# INSERT /


# def create_database(db_name):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password=""
#     )

#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE %s" % db_name)

#     print("{} database created successfully.".format(db_name))


# Retrieves data from all the columns from "table_name"
# SQL = SELECT * FROM "table_name"
# def select_all_columns(table_name):
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM {}".format(table_name))

#     myresult = mycursor.fetchall()

#     print("selected all columns from {} table.".format(table_name))
#     return myresult


# Retrieves data from specified columns "column_names" from "table_name"
# SQL = SELECT "column_names" FROM "table_name"
# def select_certain_columns(table_name, column_names):
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT {} FROM {}".format(column_names, table_name))

#     myresult = mycursor.fetchall()

#     print("selected {} columns from {}.".format(column_names, table_name))
#     return myresult


# Updates "table_name" by setting the "column_name" = "value" where the "identifier" = "identifier_value"
# SQL = UPDATE "table_name" SET "column_name" = "value" WHERE "identifier" = "identifier_value"
# def update_data(table_name, identifier, identifier_value, column_name, value):
#     mycursor = mydb.cursor()
#     mycursor.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(
#         table_name, column_name, value, identifier, identifier_value))

#     mydb.commit()

#     print("{} table updated successfully.".format(table_name))


# Deletes the row from "table_name" where the "identifier" = "identifier_value"
# SQL = DELETE FROM "table_name" WHERE "identifier" = "identifier_value"
# def delete_data(table_name, identifier, identifier_value):
#     mycursor = mydb.cursor()

#     isinstance(identifier_value, str)

#     if (not isinstance):
#         mycursor.execute("DELETE FROM {} WHERE {} = {}".format(
#             table_name, identifier, identifier_value))
#     else:
#         mycursor.execute("DELETE FROM {} WHERE {} = '{}'".format(
#             table_name, identifier, identifier_value))

#     mydb.commit()

#     print("data deleted from {} table successfully.".format(table_name))


# Deletes all data in "table_name"
# SQL = DELETE FROM "table_name"
# def delete_all(table_name):
#     mycursor = mydb.cursor()
#     mycursor.execute("DELETE FROM {}".format(table_name))

#     mydb.commit()

#     reset_index(table_name)

#     print("deleted all data from {} table successfully".format(table_name))


# Resets auto-increment index of "table_name" *Don't use (mainly for delete_all function)
# def reset_index(table_name):
#     mycursor = mydb.cursor()
#     mycursor.execute("ALTER TABLE {} AUTO_INCREMENT = 1".format(table_name))

#     mydb.commit()


# Inserts data values into "table_name"
# SQL = INSERT INTO "table_name" (columns) VALUES (values)
# data is a dictionary for e.g.
# data = {
#     "name": "William",
#     "desc": "person3"
# }
# def insert_data(table_name, data):
#     columns = []
#     values = []

#     for key, value in data.items():
#         columns.append(key)
#         values.append(value)

#     columns_string = ', '.join(f"`{w}`" for w in columns)
#     values_string = ', '.join(f"'{w}'" for w in values)

#     mycursor = mydb.cursor()
#     sql = "INSERT INTO " + table_name + \
#         " (" + columns_string + ") VALUES (" + values_string + ")"

#     mycursor.execute(sql)
#     mydb.commit()

#     print("data inserted to {} table successfully.".format(table_name))
# Test Data
# print(select_all_columns("test"))
# print("\n")
# print(select_certain_columns("test", "id, name"))
# print("\n")
# update_data("test", "id", "1", "name", "Bianca")
# print("\n")
# print(select_all_columns("test"))

# Insert
# insert_data("test", data)
# Delete
# print("\n")
# delete_data("test", "id", "5")
# delete_all("test")
# data = {
#     "food_name": "pineapple",
#     "price": 5.00,
#     "weight": 500,
#     "calories": 100
# }

# food_item_values = [
#     (
#         47,
#         "banana",
#         4.00,
#         100,
#         10
#     )
# ]

# receipts = [
#     (
#         1
#     )
# ]

# a = SQL_Database()
# print(select_data(table_name="food_item"))
# a.insert_data(table_name="receipt", table_columns=["uid"], values=receipts)
# a.insert_data(table_name="food_item", table_columns=["fid", "food_name", "price", "weight", "calories"], values=food_item_values)
# a.delete_data(table_name="food_item", identifier="fid", identifier_value="47")
# a.delete_data(table_name="test")
# a.update_data("food_item", data=data, identifier="fid", identifier_value="47")

