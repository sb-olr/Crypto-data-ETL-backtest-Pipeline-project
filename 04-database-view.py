#!/usr/bin/env python3
import sqlite3
from icecream import ic
# import my_utils

db_name = 'data/TEST-crypto-db.sqlite3'


def view_all_records(table_name):
    # Connect to database
    conn = sqlite3.connect(db_name)
    # Create a cursor
    cur=conn.cursor()

    sql_select = 'SELECT * FROM ' + table_name + ';'

    ic(sql_select)
    cur.execute(sql_select)
    rows = cur.fetchall()
    ic(rows)
    ic('query executed')

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()


def main():
    table_name = 'exchange_rates'
    view_all_records(table_name)


if __name__ == '__main__':
    main()

