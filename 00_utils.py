import datetime
import csv

def get_date_yesterday(): return str(datetime.date.today() - \
    datetime.timedelta(days=1))

def output_csv(outfile, headers, data):
    with open(outfile, 'w') as file:
        csv_file=csv.writer(file)
        csv_file.writerow(headers)
        for row in data:
            csv_file.writerow(row)

def main():
    print('test:')
    headers=('name', 'age')
    outfile='my_tools-test.csv'
    data=[('A', 10),('B', 12)]
    output_csv(outfile, headers, data)
    
    
    
if __name__=='__main__':
    main()

