#!/usr/bin/env python3
# Usage: ./02-json-to-csv.py
import requests
from icecream import ic
import my_utils

def get_data(url):
    ic(url)
    data=None
    res = requests.get(url)
    res.raise_for_status()
    if res.status_code == 200:
        data = res.json()['rates']

    return data


def reshape_data(data):
    shaped_data = []
    for key in data.keys():
        row = data[key]
        shaped_data.append((key, row['name'], row['unit'], row['value'], row['type']))
    return shaped_data


def main():
    # config
    url='https://api.coingecko.com/api/v3/exchange_rates'
    output_file='data/exchange-rate.csv'
    headers=('cur_id', 'name', 'unit', 'value', 'type')

    data = get_data(url)
    if data != None:
        shaped_data = reshape_data(data)
        my_utils.output_csv(output_file, headers, shaped_data)
        ic('CSV created')


if __name__ == '__main__':
    main()
