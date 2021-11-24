from abc import abstractclassmethod
import mysql.connector
import os

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../','.env')
load_dotenv(dotenv_path)

SQL_USERNAME = os.environ.get("SQL_USERNAME")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_DATABASE = os.environ.get("SQL_DATABASE")

def listToStr(listOfData):
    """Convert list to a string with coma separated"""
    return ",".join(listOfData)

def concatList(list1:list =None, list2:list = None, char:str = "="):
    combine = zip(list1, list2)
    result = []
    for ele1 , ele2 in combine:
        result.append("'" +ele1 + "'" + char + "'" + ele2 + "'")
    return result

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
class SQL_Database:
    """Class represents sql dataabase, and contains attributes and methods pertaining to SQL"""
    def __init__(self) -> None:
        # __Query.__init__()
        self.db = mysql.connector.connect(
            host="localhost",
            user=SQL_USERNAME,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
        self.cursor = self.db.cursor()

    def select_data(self, getheaders:list = None, filterBy:list = None, filterVal:list =None, table_name:str = None):
        """SQL Query data based on 3 inputs headers, values and table name.

        headers: Type of list. Header name
        col_values: Type of list. Values corresponding to given headers
        table_name: Type of str. String representation of table
        ."""
        if table_name is None or table_name.isspace():
            raise ValueError("Table name cannot be Null value or whitespace characters")

        if getheaders is None and filterBy is None and filterVal is None:
            self.cursor.execute(f"SELECT * from {table_name}")
        else:
            if len(filterBy) != len(filterVal):
                raise ValueError("Lists of filterBy and filterVal have different length")

            if filterBy is None:
                cols = listToStr(getheaders)
                self.cursor.execute(f"SELECT {cols} from {table_name}")
            elif getheaders is None:
                where = concatList(filterBy, filterVal)
                self.cursor.execute(f"SELECT * from {table_name} WHERE {where}")        
        return self.cursor.fetchall()

    # def delete_data(self, table_name:str, filterBy:list = None, filterVal:list =None):
    #     if table_name is None or table_name.isspace():
    #         raise ValueError("Table name cannot be Null value or whitespace characters")
    #     if filterBy is None and filterVal is None:
    #         self.cursor.execute(f"DELETE FROM {table_name}")
    #     elif len(filterBy) != len(filterVal):
    #         raise ValueError("Lists of filterBy and filterVal have different length")
    #     else:
    #         self.cursor.execute(f'DELETE FROM {table_name} WHERE {concatList(filterBy, filterVal)}')
    #     self.db.commit()

    # def insert_data(self, table_name:str, data:dict):
    #     if table_name is None or table_name.isspace():
    #         raise ValueError("Table name cannot be Null value or whitespace characters")
    #     if data is not None:
    #         cols = ', '.join(f"`{w}`" for w in data.keys())
    #         vals = ', '.join(f"'{w}'" for w in data.values())
    #         print(f'INSERT INTO {table_name} ({cols}) VALUES ({vals});')
    #         self.cursor.execute(f'INSERT INTO {table_name} ({cols}) VALUES ({vals});')
    #     self.db.commit()

    # def update_data(self, table_name:str, data:dict, filterBy:list, filterVal:str):
    #     if table_name is None or table_name.isspace():
    #         raise ValueError("Table name cannot be Null value or whitespace characters")
    #     if data is not None:
    #         set = listToStr(concatList(data.keys(), data.values()))
    #         whrCols = ', '.join(f"`{w}`" for w in filterBy)
    #         whrVal =  ', '.join(f"`{w}`" for w in filterVal)
    #         cols = ', '.join(f"`{w}`" for w in data.keys())
    #         vals = ', '.join(f"'{w}'" for w in data.values())
    #         self.cursor.execute(f'UPDATE {table_name} SET {set} WHERE {where};')
    
    
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ict2103project_database"
# )


def __listToStr(listOfData):
    """Convert list to a string with coma separated"""
    return ",".join(listOfData)


def __concatList(list1: list = None, list2: list = None, char: str = "="):
    combine = zip(list1, list2)
    result = []
    for ele1, ele2 in combine:
        result.append(ele1 + char + ele2)

    return result

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


# Adds foreign key "foreign_key" to table "table_name"
# SQL = ALTER TABLE "table_name" ADD FOREIGN KEY ("foreign_key") REFERENCES "reference_table"(reference_key)
def add_foreign_key(table_name, foreign_key, reference_table, reference_key):
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE {} ADD FOREIGN KEY ({}) REFERENCES {}({})".format(table_name, foreign_key, reference_table, reference_key))

    mydb.commit()
    
    print("Foreign key constraint on {} added to {} table".format(foreign_key, table_name))


# Test Data
# print(select_all_columns("test"))
# print("\n")
# print(select_certain_columns("test", "id, name"))
# print("\n")
# update_data("test", "id", "1", "name", "Bianca")
# print("\n")
# print(select_all_columns("test"))

# print(select_columns("edit_history", "id, edited_by"))
# print("\n")

# update_data("test", "id", "1", "name", "Bianca")
# print("\n")

# print(select_all_columns("test"))
# print("\n")

# print(add_foreign_key("edit_history", "product_id", "product", "id"))
# print("\n")

# data = {
#     "name": "William",
#     "desc": "person3"
# }

# Insert
# insert_data("test", data)

# Delete
# print("\n")
# delete_data("test", "id", "5")
# delete_all("test")


# a = SQL_Database()
# print(a.update_data(table_name="user",data=data, filterBy=["name"], filterVal=["william"]))
# print(a.insert_data(table_name="user", data=data))
