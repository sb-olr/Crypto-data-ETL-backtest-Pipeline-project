import datetime
import csv
import shutil
import os
from icecream import ic

def get_date_yesterday(): return str(datetime.date.today() -
                                     datetime.timedelta(days=1))


def output_csv(outfile, headers, data):
    with open(outfile, 'w') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(headers)
        for row in data:
            csv_file.writerow(row)


def get_list_from_csv(csv_name, skip_header=True):
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        if skip_header:
            data = data[1:]
        return data


def create_file(filename):
    f = open(filename, 'wt')
    f.close()


def delete_file(filename):
    os.remove(filename)
    ic('file delete done')


def move_file(filename, dest=destination_dir):
    shutil.move(filename, dest)
    ic('move file done')


def main():
    print('test:')
    headers = ('name', 'age')
    outfile = 'my_tools-test.csv'
    data = [('A', 10), ('B', 12)]
    output_csv(outfile, headers, data)


if __name__ == '__main__':
    main()
