#!/usr/bin/env python3
import sqlite3
from icecream import ic
import my_db_utils

db_name = 'data/TEST-crypto-db.sqlite3'

def main():
    table_name = 'exchange_rates'
    data = my_db_utils.get_all_records(db_name, table_name)
    print(data)

if __name__ == '__main__':
    main()

