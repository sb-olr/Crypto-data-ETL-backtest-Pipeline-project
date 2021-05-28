#!/usr/bin/env python3
# Usage: ./07-local-api-view.py
from icecream import ic
import my_utils
from os import system
from config import CONFIG

local_base_url = CONFIG['local_base_url']
table_name = CONFIG['table_name']
local_demo_file = CONFIG['data_dir']+CONFIG['local_json_file']

url = local_base_url+table_name
my_utils.curl_json_from_url(url, local_demo_file)
