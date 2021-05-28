#!/usr/bin/env python3
# Usage: ./ETL_pipeline.py
from os import system
from my_utils import pause
from icecream import ic

DEMO = False


# step 0: setup
if DEMO:
    system('clear')
    system('tree data')
    pause()


# step 1: create database, and table
system('clear')
ic('step 1: create database, and table')
system('./01-create-db.py')
if DEMO:
    system('tree data')
    pause()


# step 2: create csv from api endpoint
system('clear')
ic('step 2: create csv from api endpoint')
system('./02-api-to-csv.py')
if DEMO:
    system('tree data')
    pause()


# step 3: import data into database
system('clear')
ic('step 3: import data into database')
system('./03-csv-to-sqlite.py')
if DEMO:
    system('tree data')
    pause()


# step 4: move csv to a backup folder
system('clear')
ic('step 4: move csv to a backup folder')
system('./04-move-file.py')
if DEMO:
    system('tree data')
    pause()


# step 5: view table data
if DEMO:
    system('clear')
    ic('step 5: view table data')
    system('./05-database-view.py')
    system('tree data')
    pause()


# step 6: Check that sever.py is running
if DEMO:
    system('clear')
    ic('Ensure that server.py is running')
    pause()


# step 7: Check our served json
if DEMO:
    system('clear')
    ic('Check our served json')
    system('./07-local-api-view.py')
    # curl http://0.0.0.0:5000/api/view/exchange_rates | jq > data/demo.json
    pause()
    system('tree data')
    system('cat data/demo.json')
    pause()


# step 8: Teardown
if DEMO:
    system('clear')
    ic('Deleting data files')
    system('rm data/csv/processed/*')
    system('rm data/csv/*.*')
    system('rm data/*.*')
    system('tree data')
    pause()
