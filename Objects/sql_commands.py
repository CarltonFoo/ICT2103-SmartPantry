import mysql.connector
from Objects.createTables import setUpDB

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
        else:
            cols = listToStr(getheaders)
            where = concatList(filterBy, filterVal)
            cursor.execute(f"SELECT {cols} from {table_name} WHERE {where}")

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


def create_table(table_name: str, dir: str):
    if table_name is None or table_name.isspace():
        raise ValueError("Table name cannot be Null value or whitespace characters")
    setUpDB(db,dir)
    db.commit()