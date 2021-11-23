import mysql.connector
import os

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ['SQL_USERNAME'],
    password=os.environ['SQL_PASSWORD'],
    database="smartpantry"
)


def __listToStr(listOfData):
    """Convert list to a string with coma separated"""
    return ",".join(listOfData)


def __concatList(list1: list = None, list2: list = None, char: str = "="):
    combine = zip(list1, list2)
    result = []
    for ele1, ele2 in combine:
        result.append(ele1 + char + ele2)

    return result

# Things to do: create functions for the following SQL statements
# SELECT /
# UPDATE /
# DELETE /
# INSERT /


# ["*"] Retrieves data from "table_name" or ["column_names"] Retrieves data from specified columns "column_names" from "table_name"
# SQL = SELECT * FROM "table_name" or SELECT "column_names" FROM "table_name"

def select_data(self, getheaders: list = None, filterBy: list = None, filter_values: list = None, table_name: str = None):
    """SQL Query data based on 3 inputs headers, values and table name.
    headers: Type of list. Header name
    col_values: Type of list. Values corresponding to given headers
    table_name: Type of str. String representation of table
    ."""
    try:
        if len(getheaders) != len(filter_values):
            raise ValueError(
                "Lists of headers and values have different length")
        if table_name is None:
            raise ValueError("Table name is empty")

        if getheaders is None and filterBy is None:
            self.cursor.execute(f"selected * columns from {table_name}")
        elif filterBy is None:
            self.cursor.execute(
                f"selected {__listToStr(getheaders)} columns from {table_name}")
        elif getheaders is None:
            self.cursor.execute(
                f"SELECT * columns from {table_name} WHERE {__concatList(filterBy, filter_values)}")
    finally:
        self.cursor.close()
        print("cur closed")


def select_columns(selection=None, table_name=None, where=None):
    msg = ""
    try:
        if (selection == "*") and where:
            sql = "SELECT * FROM {} WHERE {}".format(table_name, where)
            msg = "selected all columns from {} table where {}.".format(table_name, where)
        elif (selection == "*") and not where:
            sql = "SELECT * FROM {}".format(table_name,)
            msg = "selected all columns from {} table.".format(table_name)
        elif not selection and where:
            sql = "SELECT {} FROM {} WHERE {}".format(selection, table_name, where)
            msg = "selected {} columns from {} where {}.".format(
                selection, table_name, where)
        elif where:
            sql = "SELECT {} FROM {}".format(selection, table_name)
            msg = "selected {} columns from {}.".format(
                selection, table_name)
            
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        return myresult
    finally:
        mycursor.close()
        print("cur closed")


# Updates "table_name" by setting the "column_name" = "value" where the "identifier" = "identifier_value"
# SQL = UPDATE "table_name" SET "column_name" = "value" WHERE "identifier" = "identifier_value"
def update_data(table_name, identifier, identifier_value, column_name, value):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(
        table_name, column_name, value, identifier, identifier_value))

    mydb.commit()

    print("{} table updated successfully.".format(table_name))


# Deletes the row from "table_name" where the "identifier" = "identifier_value"
# SQL = DELETE FROM "table_name" WHERE "identifier" = "identifier_value"
def delete_data(table_name, identifier, identifier_value):
    mycursor = mydb.cursor()

    isinstance(identifier_value, str)

    if (not isinstance):
        mycursor.execute("DELETE FROM {} WHERE {} = {}".format(
            table_name, identifier, identifier_value))
    else:
        mycursor.execute("DELETE FROM {} WHERE {} = '{}'".format(
            table_name, identifier, identifier_value))

    mydb.commit()

    print("data deleted from {} table successfully.".format(table_name))


# Deletes all data in "table_name"
# SQL = DELETE FROM "table_name"
def delete_all(table_name):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM {}".format(table_name))

    mydb.commit()

    reset_index(table_name)

    print("deleted all data from {} table successfully".format(table_name))


# Resets auto-increment index of "table_name" *Don't use (mainly for delete_all function)
def reset_index(table_name):
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE {} AUTO_INCREMENT = 1".format(table_name))

    mydb.commit()


# Inserts data values into "table_name"
# SQL = INSERT INTO "table_name" (columns) VALUES (values)
# data is a dictionary for e.g.
# data = {
#     "name": "William",
#     "desc": "person3"
# }
def insert_data(table_name, data):
    columns = []
    values = []

    for key, value in data.items():
        columns.append(key)
        values.append(value)

    columns_string = ', '.join(f"`{w}`" for w in columns)
    values_string = ', '.join(f"'{w}'" for w in values)

    mycursor = mydb.cursor()
    sql = "INSERT INTO " + table_name + \
        " (" + columns_string + ") VALUES (" + values_string + ")"

    mycursor.execute(sql)
    mydb.commit()

    print("data inserted to {} table successfully.".format(table_name))


# Adds foreign key "foreign_key" to table "table_name"
# SQL = ALTER TABLE "table_name" ADD FOREIGN KEY ("foreign_key") REFERENCES "reference_table"(reference_key)
def add_foreign_key(table_name, foreign_key, reference_table, reference_key):
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE {} ADD FOREIGN KEY ({}) REFERENCES {}({})".format(table_name, foreign_key, reference_table, reference_key))

    mydb.commit()
    
    print("Foreign key constraint on {} added to {} table".format(foreign_key, table_name))


# Test Data
# print(select_columns("edit_history", "*"))
# print("\n")

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
