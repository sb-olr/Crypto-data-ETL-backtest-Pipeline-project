#!/usr/bin/env python3
# Usage: ./01-create-db.py
import my_db_utils

# db_name = ':memory:' # to make a in memory db
db_name = 'data/TEST-crypto-db.sqlite3'
table_name = 'exchange_rates'
table_fields = ('cur_id TEXT', 'name TEXT', 'unit TEXT',
                'value REAL', 'type TEXT', 'date TEXT')
my_db_utils.create_table(db_name, table_name, table_fields)