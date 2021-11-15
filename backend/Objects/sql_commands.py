import mysql.connector

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ict2103project_database"
)

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


def select_all_columns(table_name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {}".format(table_name))

    myresult = mycursor.fetchall()

    print("selected all columns from {} table.".format(table_name))
    return myresult


def select_certain_columns(table_name, column_names):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT {} FROM {}".format(column_names, table_name))

    myresult = mycursor.fetchall()

    print("selected {} columns from {}.".format(column_names, table_name))
    return myresult


def update_data(table_name, identifier, identifier_value, column_name, value):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(
        table_name, column_name, value, identifier, identifier_value))

    mydb.commit()

    print("{} table updated successfully.".format(table_name))


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


def delete_all(table_name):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM {}".format(table_name))

    mydb.commit()

    reset_index(table_name)

    print("deleted all data from {} table successfully".format(table_name))


def reset_index(table_name):
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE {} AUTO_INCREMENT = 1".format(table_name))

    mydb.commit()


def insert_data(table_name, columns, values):
    mycursor = mydb.cursor()
    sql = "INSERT INTO " + table_name + \
        " (" + columns + ") VALUES (" + values + ")"

    mycursor.execute(sql)
    mydb.commit()

    print("data inserted to {} table successfully.".format(table_name))


# Test Data
print(select_all_columns("test"))
print("\n")
print(select_certain_columns("test", "id, name"))
print("\n")
update_data("test", "id", "1", "name", "Bianca")
print("\n")
print(select_all_columns("test"))

# Insert
columns = ["name", "desc"]
columns_string = ', '.join(f"`{w}`" for w in columns)

values = ["Grace", "person4"]
values_string = ', '.join(f"'{w}'" for w in values)
# insert_data("test", columns_string, values_string)

# Delete
print("\n")
# delete_data("test", "id", "4")
# delete_all("test")
