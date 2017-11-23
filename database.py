import os
import time
import datetime
import mysql.connector
from mysql.connector import errorcode
from wikitables import import_tables


DB_NAME = 'inhomenursing'

TABLES = {}
TABLES['food'] = (
    "CREATE TABLE food ("
    "   id int(4) AUTO_INCREMENT,"
    "   thai VARCHAR(30) UNIQUE,"
    "   script VARCHAR(30) UNIQUE,"
    "   english VARCHAR(30),"
    "   description TEXT,"
    "   PRIMARY KEY (id)"
    ") ENGINE=InnoDB")

TABLES['routine'] = (
    "CREATE TABLE routine ("
    "   time CHAR(20) NOT NULL,"
    "   food VARCHAR(30),"
    "   PRIMARY KEY (time)"
    ") ENGINE=InnoDB")

FIELDS = {}
FIELDS['food'] = ('thai', 'script', 'english', 'description')

FIELDS['routine'] = ('datetime', 'food')

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
}


def create_database():
    try:
        cursor.execute('''
            CREATE DATABASE {}
                DEFAULT CHARACTER SET utf8
                DEFAULT COLLATE utf8_general_ci
            '''.format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_table(name, ddl):
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# def insert_into(table_name, fields, values):
#     insert = ("INSET INTO {} ({}) VALUES ({})".format(
#         table_name, ', '.join(fields), ', '.join(values)))
#     cursor.execute(insert)
#     cursor.execute('''
#         INSERT INTO %s (%s, %s, %s, %s)
#         VALUES (%s, %s, %s, %s)
#         ''', table_name, *fields, tname, script, ename, desc)
#     db.commit()


def insert_food(tname, script, ename, desc):
    cursor.execute('''
        INSERT IGNORE INTO food(thai, script, english, description)
        VALUES (%s, %s, %s, %s)''', (tname, script, ename, desc))
    db.commit()


def insert_routine(now, food):
    cursor.execute('''
        INSERT IGNORE INTO routine(time, food)
        VALUES (%s, %s)''', (now, food))
    db.commit()


def query_data():
    cursor.execute('''
        SELECT id, thai FROM food
        ORDER BY id''')
    for foodid, thai in cursor:
        print('Food ID: {} Thai Script: {}'.format(foodid, thai))


def search(food):
    query = ("SELECT thai FROM food WHERE thai = '{}'".format(food))
    cursor.execute(query)
    if (res for res in cursor if res == food):
        return True
    else:
        return False

db = mysql.connector.connect(**config)
cursor = db.cursor(buffered=True)

# CONNECT DATABASE IF NOT EXISTS CREATE DATEBASE
try:
    db.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database()
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

# CREATE TABLE
for name, ddl in TABLES.items():
    create_table(name, ddl)


tables = import_tables('List of Thai dishes')

for numTab in range(0, 15):
    for row in tables[numTab].rows[:len(tables[numTab].rows)-1]:
        thai_name = str(row['Thai name'])
        thai_script = str(row['Thai script'])
        if 'http' in thai_script:
            thai_script = thai_script.split()[1].strip(']')
        english_name = str(row['English name'])
        if english_name == '<!-- English name -->':
            english_name = 'None'
        description = str(row['Description'])
        insert_food(thai_name, thai_script, english_name, description)
