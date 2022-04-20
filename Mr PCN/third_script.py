import mysql.connector
import os
from dotenv import load_dotenv
from database_server import check_owner, cursor 

load_dotenv()

db_table = os.getenv('DB_TABLE')
db_table_2 = os.getenv('DB_TABLE_2')
db = mysql.connector.connect(
    host = os.getenv('DB_HOST_2'),
    user = os.getenv('DB_USER_2'),
    passwd = os.getenv('DB_PASS_2'),
    database = os.getenv('DB_DATABASE_2')
)


local_cursor = db.cursor()

cursor.execute(f"SELECT owner_name FROM {db_table}")
users_with_email = [i[0] for i in cursor.fetchall()]

print(users_with_email)

