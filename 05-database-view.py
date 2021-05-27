#!/usr/bin/env python3
# Usage: ./05-database-view.py
from icecream import ic
import my_db_utils
from config import CONFIG

db_name = CONFIG['data_dir']+CONFIG['db_file']
table_name = CONFIG['table_name']

data = my_db_utils.get_all_records(db_name, table_name)
ic(data)
