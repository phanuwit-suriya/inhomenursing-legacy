import os
import mysql.connector
from mysql.connector import errorcode
from wikitables import import_tables


def create_database():
    try:
        cursor.execute('''
            CREATE DATABASE inhomenursing
            ''')
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_table():
    try:
        cursor.execute('''
            CREATE TABLE foods(
                foodID int(4) PRIMARY KEY AUTO_INCREMENT,
                foodThaiName VARCHAR(20),
                foodThaiScript VARCHAR(30),
                foodEnglishName VARCHAR(30),
                foodDescription TEXT)
            ''')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def insert_table(thai_name, thai_script, english_name, description):
    cursor.execute('''
        INSERT INTO foods(foodThaiName, foodThaiScript, foodEnglishName, foodDescription)
        VALUES(%s, %s, %s, %s)''', (thai_name, thai_script, english_name, description))
    db.commit()


def querying_data():
    cursor.execute('''
        SELECT foodThaiName, foodDescription FROM foods
        ''')
    for (thai_name, description) in cursor:
        print('Thai Name: {}\nThai Script: {}\n'.format(thai_name, description))


tables = import_tables('List of Thai dishes')

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    # 'database': 'inhomenursing'
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
try:
    db.database = 'inhomenursing'
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database()
        db.database = "inhomenursing"
    else:
        print(err)
        exit(1)

create_table()

for numTab in range(0,15):
    for row in tables[numTab].rows[:len(tables[numTab].rows)-1]:
        thai_name = str(row['Thai name'])
        thai_script = str(row['Thai script'])
        if 'http' in thai_script:
            thai_script = thai_script.split()[1].strip(']')
        english_name = str(row['English name'])
        if english_name == '<!-- English name -->':
            english_name = None
        description = str(row['Description'])
        insert_table(thai_name, thai_script, english_name, description)

querying_data()
cursor.close()
db.close()
