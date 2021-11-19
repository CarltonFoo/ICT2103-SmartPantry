import mysql.connector
import os

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    # user=os.environ['SQL_USERNAME'],
    # password=os.environ['SQL_PASSWORD'],
    user = "root",
    password = "",
    database="smartpantry"
)

# Things to do: create functions for the following SQL statements
# SELECT /
# UPDATE /
# DELETE /
# INSERT /


# ["*"] Retrieves data from "table_name" or ["column_names"] Retrieves data from specified columns "column_names" from "table_name"
# SQL = SELECT * FROM "table_name" or SELECT "column_names" FROM "table_name"
def select_columns(table_name, selection):
    msg = ""
    
    if (selection == "*"):
        sql = "SELECT * FROM {}".format(table_name)
        msg = "selected all columns from {} table.".format(table_name)
    else:
        sql = "SELECT {} FROM {}".format(selection, table_name)
        msg = "selected {} columns from {}.".format(selection, table_name)
        
    mycursor = mydb.cursor()
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    print(msg)
    return myresult


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
