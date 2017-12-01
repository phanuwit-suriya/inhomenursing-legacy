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
    "   food_thai VARCHAR(30) UNIQUE,"
    "   food_script VARCHAR(30) UNIQUE,"
    "   food_english VARCHAR(30),"
    "   food_description TEXT,"
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
    "   `serving_size` TEXT,"
    "   `calories(kcal)` FLOAT,"
    "   `cal_fat(kcal)` FLOAT,"
    "   `total_fat(g)` FLOAT,"
    "   `sat_fat(g)` FLOAT,"
    "   `polyunsat_fat(g)` FLOAT,"
    "   `monounsat_fat(g)` FLOAT,"
    "   `trans_fat(g)` FLOAT,"
    "   `cholesterol(mg)` FLOAT,"
    "   `sodium(mg)` FLOAT,"
    "   `potassium(mg)` FLOAT,"
    "   `total_carb(g)` FLOAT,"
    "   `diet_fiber(g)` FLOAT,"
    "   `sugar(g)` FLOAT,"
    "   `protein(g)` FLOAT,"
    "   `total_fat(%)` FLOAT,"
    "   `sat_fat(%)` FLOAT,"
    "   `cholesterol(%)` FLOAT,"
    "   `sodium(%)` FLOAT,"
    "   `potassium(%)` FLOAT,"
    "   `total_carb(%)` FLOAT,"
    "   `diet_fiber(%)` FLOAT,"
    "   `protein(%)` FLOAT,"
    "   `vit_a(%)` FLOAT,"
    "   `vit_c(%)` FLOAT,"
    "   `calcium(%)` FLOAT,"
    "   `iron(%)` FLOAT,"
    "   `vit_d(%)` FLOAT,"
    "   `vit_b6(%)` FLOAT,"
    "   `vit_b12(%)` FLOAT,"
    "   `magnesium(%)` FLOAT,"
    "   `thaimin(%)` FLOAT,"
    "   `riboflavin(%)` FLOAT,"
    "   `niacin(%)` FLOAT,"
    "   `vit_e(%)` FLOAT,"
    "   `vit_k(%)` FLOAT,"
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
        print('Creating table {}: '.format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('already exists.')
        else:
            print(err.msg)
    else:
        print("OK")


def insert_food(tname, script, ename, desc):
    try:
        cursor.execute('''
            INSERT IGNORE INTO food(food_thai, food_script, food_english, food_description)
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


def insert_nutrition(name, serving_size, calories, cal_fat, total_fat, sat_fat, poly_fat, mono_fat, trans_fat, cholesterol, sodium, potassium, total_carb, diet_fiber, sugar, protein, percent_total_fat, percent_sat_fat, percent_cholesterol, percent_sodium, percent_potassium, percent_total_carb, percent_diet_fiber, percent_protein, vit_a, vit_c, calcium, iron, vit_d, vit_b6, vit_b12, magnesium, thiamin, riboflavin, niacin, vit_e, vit_k, zinc, phosphorus):
    try:
        cursor.execute('''
            INSERT IGNORE INTO nutrition(`name`, `serving_size`, `calories(kcal)`, `cal_fat(kcal)`, `total_fat(g)`, `sat_fat(g)`, `polyunsat_fat(g)`, `monounsat_fat(g)`, `trans_fat(g)`, `cholesterol(mg)`, `sodium(mg)`, `potassium(mg)`, `total_carb(g)`, `diet_fiber(g)`, `sugar(g)`, `protein(g)`, `total_fat(%)`, `sat_fat(%)`, `cholesterol(%)`, `sodium(%)`, `potassium(%)`, `total_carb(%)`, `diet_fiber(%)`, `protein(%)`, `vit_a(%)`, `vit_c(%)`, `calcium(%)`, `iron(%)`, `vit_d(%)`, `vit_b6(%)`, `vit_b12(%)`, `magnesium(%)`, `thaimin(%)`, `riboflavin(%)`, `niacin(%)`, `vit_e(%)`, `vit_k(%)`, `zinc(%)`, `phosphorus(%)`)
            VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s)''', (name, serving_size, calories, cal_fat, total_fat, sat_fat, poly_fat, mono_fat, trans_fat, cholesterol, sodium, potassium, total_carb, diet_fiber, sugar, protein, percent_total_fat, percent_sat_fat, percent_cholesterol, percent_sodium, percent_potassium, percent_total_carb, percent_diet_fiber, percent_protein, vit_a, vit_c, calcium, iron, vit_d, vit_b6, vit_b12, magnesium, thiamin, riboflavin, niacin, vit_e, vit_k, zinc, phosphorus))
        db.commit()
    except Exception as e:
        print(e)


def food_search(food):
    query = "SELECT thai FROM food WHERE thai = '{}'".format(food)
    try:
        cursor.execute(query)
        for res in cursor:
            if res[0] == food:
                return True
            else:
                return False
    except Exception as e:
        print(e)


def nutrition_search(food):
    query = "SELECT * FROM nutrition WHERE name LIKE '%{}%'".format(food)
    try:
        cursor.execute(query)
        for res in cursor:
            if food in res[1]:
                return True
            else:
                return False
    except Exception as e:
        print(e)


def routine_search(date):
    query = "SELECT DISTINCT r.time, f.food_thai, f.food_script, f.food_english, f.food_description FROM food f JOIN routine r ON f.food_thai LIKE CONCAT(r.food) WHERE r.time LIKE '{}%' ORDER BY r.time".format(
        date)
    try:
        cursor.execute(query)
        for res in cursor:
            print('Time: {}\nFood: {}({}, {})\nfood_description: {}'.format(
                res[0], res[3], res[1], res[2], res[4]))
    except Exception as e:
        print(e)


db = mysql.connector.connect(**config)
cursor = db.cursor(buffered=True)

# CONNECT DATABASE IF NOT EXISTS CREATE DATEBASE
try:
    db.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database()
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

# CREATE TABLE, FIRST TIME USING ONLY
# for name, ddl in TABLES.items():
#     create_table(name, ddl)

# tables = import_tables('List of Thai dishes')

# for numTab in range(0, 15):
#     for row in tables[numTab].rows[:len(tables[numTab].rows)-1]:
#         thai_name = str(row['Thai script'])
#         if 'http' in thai_name:
#             thai_name = thai_name.split()[1].strip(']')
#         thai_script = str(row['Thai name'])
#         english_name = str(row['English name'])
#         if english_name == '<!-- English name -->' or english_name == '':
#             english_name = None
#         food_description = str(row['Description'])
#         insert_food(thai_name, thai_script, english_name, food_description)
