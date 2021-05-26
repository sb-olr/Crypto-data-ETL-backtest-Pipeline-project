#!/usr/bin/env python3
import sqlite3
from icecream import ic
import my_utils

db_name = 'data/TEST-crypto-db.sqlite3'


def csv_to_sqlite(csv_name, table_name):
    # today
    dt_today = '2021-05-25'
    # get data from csv
    rows=my_utils.get_list_from_csv(csv_name)
    rows = [r+[dt_today] for r in rows]
    ic(rows)


    # Connect to database
    conn = sqlite3.connect(db_name)
    # Create a cursor
    cur=conn.cursor()

    sql_insert = 'INSERT INTO ' + table_name + ' VALUES (? ,? ,?, ?, ?, ?);'

    ic(sql_insert)
    cur.executemany(sql_insert, rows)
    ic('insert completed')

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()


def main():
    csv_name = 'data/exchange-rate.csv'
    table_name = 'exchange_rates'
    csv_to_sqlite(csv_name, table_name)


if __name__ == '__main__':
    main()

