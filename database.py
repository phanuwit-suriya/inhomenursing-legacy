import os
import time
import datetime
import mysql.connector
from mysql.connector import errorcode
from wikitables import import_tables

# DATABASE NAME
DB_NAME = 'inhomenursing'

# TABLE INFO
TABLES = {}
TABLES['food'] = (
    "CREATE TABLE food ("
    "   food_id INT NOT NULL AUTO_INCREMENT,"
    "   thaiName VARCHAR(30) UNIQUE,"
    "   thaiScript VARCHAR(30) UNIQUE,"
    "   englishName VARCHAR(30),"
    "   description TEXT,"
    "   PRIMARY KEY (food_id)"
    ") ENGINE=InnoDB")

TABLES['routine'] = (
    "CREATE TABLE routine ("
    "   time INT NOT NULL,"
    "   food VARCHAR(30),"
    "   PRIMARY KEY (time)"
    ") ENGINE=InnoDB")

TABLES['nutrition'] = (
    "CREATE TABLE nutrition ("
    "   `nutrition_id` INT AUTO_INCREMENT,"
    "   `name` VARCHAR(100),"
    "   `servingSize` TEXT,"
    "   `calories(kcal)` FLOAT,"
    "   `calFat(kcal)` FLOAT,"
    "   `totalFat(g)` FLOAT,"
    "   `satFat(g)` FLOAT,"
    "   `polyunsatFat(g)` FLOAT,"
    "   `monounsatFat(g)` FLOAT,"
    "   `transFat(g)` FLOAT,"
    "   `cholesterol(mg)` FLOAT,"
    "   `sodium(mg)` FLOAT,"
    "   `potassium(mg)` FLOAT,"
    "   `totalCarb(g)` FLOAT,"
    "   `dietFiber(g)` FLOAT,"
    "   `sugar(g)` FLOAT,"
    "   `protein(g)` FLOAT,"
    "   `totalFat(%)` FLOAT,"
    "   `satFat(%)` FLOAT,"
    "   `cholesterol(%)` FLOAT,"
    "   `sodium(%)` FLOAT,"
    "   `potassium(%)` FLOAT,"
    "   `totalCarb(%)` FLOAT,"
    "   `dietFiber(%)` FLOAT,"
    "   `protein(%)` FLOAT,"
    "   `vitA(%)` FLOAT,"
    "   `vitC(%)` FLOAT,"
    "   `calcium(%)` FLOAT,"
    "   `iron(%)` FLOAT,"
    "   `vitD(%)` FLOAT,"
    "   `vitB6(%)` FLOAT,"
    "   `vitB12(%)` FLOAT,"
    "   `magnesium(%)` FLOAT,"
    "   `thaimin(%)` FLOAT,"
    "   `riboflavin(%)` FLOAT,"
    "   `niacin(%)` FLOAT,"
    "   `vitE(%)` FLOAT,"
    "   `vitK(%)` FLOAT,"
    "   `zinc(%)` FLOAT,"
    "   `phosphorus(%)` FLOAT,"
    "   PRIMARY KEY (nutrition_id)"
    ") ENGINE=InnoDB")

# DATABASE CONFIG
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
    try:
        cursor.execute('''
            INSERT IGNORE INTO food(thaiName, thaiScript, englishName, description)
            VALUES (%s, %s, %s, %s)''', (tname, script, ename, desc))
        db.commit()
    except Exception as e:
        print(e)


def insert_routine(now, food):
    try:
        cursor.execute('''
            INSERT IGNORE INTO routine(time, food)
            VALUES (%s, %s)''', (now, food))
        db.commit()
    except Exception as e:
        print(e)


def insert_nutrition(name, servingSize, calories, calFat, totalFat, satFat, polyFat, monoFat, transFat, cholesterol, sodium, potassium, totalCarb, dietFiber, sugar, protein, percent_totalFat, percent_satFat, percent_cholesterol, percent_sodium, percent_potassium, percent_totalCarb, percent_dietFiber, percent_protein, vitA, vitC, calcium, iron, vitD, vitB6, vitB12, magnesium, thiamin, riboflavin, niacin, vitE, vitK, zinc, phosphorus):
    try:
        cursor.execute('''
            INSERT IGNORE INTO nutrition(`name`, `servingSize`, `calories(kcal)`, `calFat(kcal)`, `totalFat(g)`, `satFat(g)`, `polyunsatFat(g)`, `monounsatFat(g)`, `transFat(g)`, `cholesterol(mg)`, `sodium(mg)`, `potassium(mg)`, `totalCarb(g)`, `dietFiber(g)`, `sugar(g)`, `protein(g)`, `totalFat(%)`, `satFat(%)`, `cholesterol(%)`, `sodium(%)`, `potassium(%)`, `totalCarb(%)`, `dietFiber(%)`, `protein(%)`, `vitA(%)`, `vitC(%)`, `calcium(%)`, `iron(%)`, `vitD(%)`, `vitB6(%)`, `vitB12(%)`, `magnesium(%)`, `thaimin(%)`, `riboflavin(%)`, `niacin(%)`, `vitE(%)`, `vitK(%)`, `zinc(%)`, `phosphorus(%)`)
            VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s)''', (name, servingSize, calories, calFat, totalFat, satFat, polyFat, monoFat, transFat, cholesterol, sodium, potassium, totalCarb, dietFiber, sugar, protein, percent_totalFat, percent_satFat, percent_cholesterol, percent_sodium, percent_potassium, percent_totalCarb, percent_dietFiber, percent_protein, vitA, vitC, calcium, iron, vitD, vitB6, vitB12, magnesium, thiamin, riboflavin, niacin, vitE, vitK, zinc, phosphorus))
        db.commit()
    except Exception as e:
        print(e)


def query_data():
    try:
        cursor.execute('''
            SELECT id, thai FROM food
            ORDER BY id''')
        for foodid, thai in cursor:
            print('Food ID: {} Thai Script: {}'.format(foodid, thai))
    except Exception as e:
        print(e)


def food_search(food):
    try:
        query = "SELECT thai FROM food WHERE thai = '{}'".format(food)
        cursor.execute(query)
        for res in cursor:
            if res[0] == food:
                return True
            else:
                return False
    except Exception as e:
        print(e)


def nutrition_search(food):
    try:
        query = "SELECT * FROM nutrition WHERE name LIKE '%{}%'".format(food)
        cursor.execute(query)
        for res in cursor:
            if food in res[1]:
                return True
            else:
                return False
    except Exception as e:
        print(e)


def routine_search(date):
    try:
        query = "SELECT DISTINCT n.* FROM nutrition n JOIN routine r ON n.name LIKE CONCAT('%', r.food, '%') WHERE r.time LIKE '%{}%'".format(
            date)
        cursor.execute(query)
        for res in cursor:
            print(res)
    except Exception as e:
        print(e)


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

# tables = import_tables('List of Thai dishes')

# for numTab in range(0, 15):
#     for row in tables[numTab].rows[:len(tables[numTab].rows)-1]:
#         thai_name = str(row['Thai script'])
#         if 'http' in thai_name:
#             thai_name = thai_name.split()[1].strip(']')
#         thai_script = str(row['Thai name'])
#         english_name = str(row['English name'])
#         if english_name == '<!-- English name -->':
#             english_name = 'None'
#         description = str(row['Description'])
#         insert_food(thai_name, thai_script, english_name, description)
