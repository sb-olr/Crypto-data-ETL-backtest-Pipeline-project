#!/usr/bin/env python3
# Usage: ./01-create-db.py
import sqlite3
from icecream import ic
# db_name = ':memory:' # to make a in memory db
db_name = 'data/TEST-crypto-db.sqlite3'


def create_table(db_name, table_name, table_fields):
    # Connect to database; creates a new one if not existing
    conn = sqlite3.connect(db_name)

    # Create a cursor
    cur=conn.cursor()

    # 5 datatypes in SQLITE:
    # NULL, INTEGER, REAL, TEXT, BLOB

    # Create a table
    # https://stackoverflow.com/questions/4098008/create-table-in-sqlite-only-if-it-doesnt-exist-already
    sql_create = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(table_fields)});'

    ic(sql_create)
    cur.execute(sql_create)

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

if __name__=='__main__':
    table_name = 'exchange_rates'
    table_fields = ('cur_id TEXT', 'name TEXT', 'unit TEXT', 'value REAL', 'type TEXT', 'date TEXT')
    create_table(db_name, table_name, table_fields)