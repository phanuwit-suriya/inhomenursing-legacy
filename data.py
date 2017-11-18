import os
import re
import sqlite3
from wikitables import import_tables


def create_table():
    cursor.execute('''
        CREATE TABLE foods(
            ThaiName VARCHAR(20),
            ThaiScript VARCHAR(30),
            EnglishName VARCHAR(30),
            Description TEXT)
        ''')
    db.commit()


def insert_table(thai_name, thai_script, english_name, description):
    cursor.execute('''
        INSERT INTO foods(ThaiName, ThaiScript, EnglishName, Description)
        VALUES(?, ?, ?, ?)''', (thai_name, thai_script, english_name, description))
    db.commit()


def select_table():
    cursor.execute('''
        SELECT ThaiName FROM foods
        ''')
    db.commit()
    table = cursor.fetchall()
    for row in table:
        print('Thai Name: {}\nThai Script: {}\nEnglish Name: {}\nDescription: {}\n'.format(row[0], row[1], row[2], row[3]))

db = sqlite3.connect('foods.db')
cursor = db.cursor()
tables = import_tables('List of Thai dishes')

if not os.path.isfile('foods.db'):
    create_table()
# for numTab in range(0,15):
#     for row in tables[numTab].rows[:len(tables[numTab].rows)-1]:
#         thai_name = str(row['Thai name'])
#         thai_script = str(row['Thai script'])
#         if 'http' in thai_script:
#             thai_script = thai_script.split()[1].strip(']')
#         english_name = str(row['English name'])
#         description = str(row['Description'])
#         insert_table(thai_name, thai_script, english_name, description)

select_table()
db.close()
