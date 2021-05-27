#!/usr/bin/env python3
# Usage: ./04-move-file.py
import os
from icecream import ic
import my_utils
from config import CONFIG


csv_dir = CONFIG['csv_dir']
processed_dir = CONFIG['processed_dir']
table_name = CONFIG['table_name']
csv_file = f'{csv_dir}{table_name}.csv'

# use move function
if os.path.isfile(csv_file):
    my_utils.move_file(csv_file, processed_dir)
    ic('csv file moved')
else:
    ic('File not found!')
