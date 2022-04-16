from flask_mysqldb import MySQL

mysql = MySQL()


def addtodb():
    cursor = mysql.connection.cursor()
    cursor.execute(f''' INSERT INTO {db_table} VALUES(%s,%s,%s,%s,%s)''', (owner_name, location_address, pcn, subdivision, legal_description)),
    mysql.connection.commit()
    cursor.close()
    return f"Done!!"



def createtable():
    cursor = mysql.connection.cursor()
    cursor.execute(f'''CREATE TABLE `{db_table}` ( `state` VARCHAR(1000) NULL , `owner_name` VARCHAR(1000) NULL , `location_address` VARCHAR(1000) NULL , `pcn` VARCHAR(20) NULL , `subdivision` VARCHAR(1000) NULL , `legal_description` VARCHAR(1000) NULL) ENGINE = InnoDB;''')
    mysql.connection.commit()
    cursor.close()
    return "The database was created Sucessfully"



# This is redirect takes care of updating the database

def updatedb():
    cursor = mysql.connection.cursor()
    cursor.execute(f'''UPDATE `{db_table}` SET  `location_address`="{location_address}",`pcn`= "{pcn}",`subdivision`= "{subdivision}",`legal_description`= "{legal_description}" WHERE `owner_name` = "{owner_name}"''')
    mysql.connection.commit()
    cursor.close()
    return "The database was updated Sucessfully"
