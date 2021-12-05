import mysql.connector

# Function takes in two parameter db which is mysql connect object and filePath which is the path to the sql script full_script
def setUpDB(db,filePath):
    cursor = db.cursor()
    fd = open(str(filePath),'r')
    sqlfile = fd.read()
    sqlCommands = sqlfile.split(";")
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print("command skipped: ", msg)
    db.commit()
    print("successfully created")
    return
