import csv
from random import sample

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample+=  countries_data.read()
    countries_dialect= csv.Sniffer().sniff(sample)
    countries_data.seek(0) #goes back to the start of the file
    country_reader = csv.reader(countries_data, delimiter='|')
    for row in country_reader:
        print(row)

print('*'*80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(countries_dialect,attribute))}')