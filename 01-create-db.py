#!/usr/bin/env python3
# Usage: ./02-json-to-csv.py
import sqlite3

# db_name = ':memory:' # to make a in memory db
db_name = 'data/crypto-db.sqlite3'

# Connect to database; creates a new one if not existing
conn = sqlite3.connect(db_name)

# Create a cursor
cur=conn.cursor()

# 5 datatypes in SQLITE:
# NULL, INTEGER, REAL, TEXT, BLOB

# Create a table
# https://stackoverflow.com/questions/4098008/create-table-in-sqlite-only-if-it-doesnt-exist-already
sql_create = '''CREATE TABLE IF NOT EXISTS exchange_rates (
    cur_id TEXT,
    name TEXT,
    unit TEXT,
    value REAL,
    type TEXT
)'''
cur.execute(sql_create)

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()
