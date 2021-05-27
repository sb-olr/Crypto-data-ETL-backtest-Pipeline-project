#!/usr/bin/env python3
import sqlite3
from icecream import ic
import my_utils, my_db_utils

db_name = 'data/TEST-crypto-db.sqlite3'


def csv_to_sqlite(csv_name, table_name):

    # get data from csv
    rows = my_utils.get_list_from_csv(csv_name)
    ic(rows)

    my_db_utils.insert_data(db_name, table_name, rows)

def main():
    table_name = 'exchange_rates'
    csv_name = 'data/exchange-rates.csv'
    csv_to_sqlite(csv_name, table_name)


if __name__ == '__main__':
    main()
