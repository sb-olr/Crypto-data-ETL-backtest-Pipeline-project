#!/usr/bin/env python3
# Usage: ./02-json-to-csv.py
from icecream import ic
import my_utils
from config import CONFIG


def get_data(url):
    data = my_utils.get_json_from_url(url)['rates']
    return data


def reshape_data(data):
    shaped_data = []

    # today
    dt_today = my_utils.get_date_today()

    for key in data.keys():
        row = data[key]
        shaped_data.append(
            (key, row['name'], row['unit'], row['value'], row['type'], dt_today))
    return shaped_data


def main():
    # config
    table_name = CONFIG['table_name']
    url = CONFIG['url']
    csv_dir = CONFIG['csv_dir']
    
    ts = my_utils.get_epoch_timestamp()
    csv_file = f'{csv_dir}{table_name}.csv'
    # csv_file = f'{csv_dir}{table_name}__{ts}.csv' # todo: use unique names

    headers = CONFIG['headers']

    data = get_data(url)
    if data != None:
        shaped_data = reshape_data(data)
        my_utils.output_csv(csv_file, headers, shaped_data)


if __name__ == '__main__':
    main()
