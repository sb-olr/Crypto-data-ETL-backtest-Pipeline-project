#!/usr/bin/env python3
import sqlite3
from icecream import ic
import my_utils


def create_table(db_name, table_name, table_fields):
    # Connect to database; creates a new one if not existing
    conn = sqlite3.connect(db_name)

    # Create a cursor
    cur = conn.cursor()

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


def insert_data(db_name, table_name, rows):
    '''
    Note: sequence of columns in data should match db schema
    '''
    # Connect to database
    conn = sqlite3.connect(db_name)
    # Create a cursor
    cur = conn.cursor()

    # nr_columns =
    mask = ', '.join(['?']*len(rows[0]))
    sql_insert = f'INSERT INTO {table_name} VALUES ({mask});'

    ic(sql_insert)
    cur.executemany(sql_insert, rows)
    ic('insert completed')

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()


def get_all_records(db_name, table_name):
    # Connect to database
    conn = sqlite3.connect(db_name)
    # Create a cursor
    cur = conn.cursor()

    sql_select = 'SELECT * FROM ' + table_name + ';'

    ic(sql_select)
    cur.execute(sql_select)
    rows = cur.fetchall()
    ic('query executed')

    # Commit the changes
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()

    return rows


def csv_to_sqlite(db_name, table_name, csv_file):
    # get data from csv
    rows = my_utils.get_list_from_csv(csv_file)
    ic('Rows available:')
    ic(len(rows))
    insert_data(db_name, table_name, rows)
    ic('imported ' + csv_file)
