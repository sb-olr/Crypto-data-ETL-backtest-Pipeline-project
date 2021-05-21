#!/usr/local/bin/python3
import sqlite3
from icecream import ic
import my_utils

db_name = 'data/crypto-db.sqlite3'
csv_name = 'data/exchange-rate.csv'
table_name = 'exchange_rates'
# get data from csv
rows=my_utils.get_list_from_csv(csv_name)

# Connect to database
conn = sqlite3.connect(db_name)
# Create a cursor
cur=conn.cursor()

sql_insert = 'INSERT INTO ' + table_name + ' VALUES (? ,? ,?, ?, ?)'

ic(sql_insert)
cur.executemany(sql_insert, rows)
ic('insert completed')

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()
