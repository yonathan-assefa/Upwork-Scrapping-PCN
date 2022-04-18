import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_table = os.getenv('DB_TABLE')
db = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    passwd = os.getenv('DB_PASS'),
    database = os.getenv('DB_DATABASE')
)


cursor = db.cursor()

def addtodb(userInfo):
    global cursor
    owner_name = userInfo['owner_name']
    location_address = userInfo['location_address']
    pcn = userInfo['pcn']
    subdivision = userInfo['subdivision']
    legal_description = userInfo['legal_description']
    cursor.execute(f" INSERT INTO {db_table} (owner_name, location_address, pcn, subdivision, legal_description) VALUES(%s,%s,%s,%s,%s)", (owner_name, location_address, pcn, subdivision, legal_description))
    db.commit()
    return f"Done!!"



def createtable():
    global cursor
    cursor.execute(f"CREATE TABLE {db_table} (owner_name VARCHAR(1000), email_id VARCHAR(255), location_address VARCHAR(1000), pcn VARCHAR(255), subdivision VARCHAR(255), legal_description VARCHAR(1000))")
    return "The database was created Sucessfully"



# This is redirect takes care of updating the database

def updatedb(userInfo):
    global cursor
    owner_name = userInfo['owner_name']
    email_id = userInfo['email_id']
    location_address = userInfo['location_address']
    pcn = userInfo['pcn']
    subdivision = userInfo['subdivision']
    legal_description = userInfo['legal_description']
    cursor.execute(f"UPDATE {db_table} SET owner_name = %s, email_id = %s, location_address = %s, pcn = %s, subdivision = %s, legal_description = %s WHERE pcn = %s", (owner_name, email_id, location_address, pcn, subdivision, legal_description, pcn))
    db.commit()

    return f"The database was updated Sucessfully, {cursor.rowcount} rows were updated"

userInfo = {
    'owner_name': 'somedude',
    'location_address': 'Am',
    'pcn': '04-00-78-99-05',
    'subdivision': 'dep',
    'legal_description': 'some desctiption here'

}

userInfo = {
    'owner_name': 'somedude',
    'email_id': 'man@gmail.com',
    'location_address': 'Am',
    'pcn': '04-00-78-99-05',
    'subdivision': 'dep',
    'legal_description': 'some desctiption here'

}


try:
    createtable()
except mysql.connector.Error as err:
    print(err)

# addtodb(userInfo)
# updatedb(userInfo)
