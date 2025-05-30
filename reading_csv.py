import csv

with open('example.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        print(i, row)
        if i == 4:
            break
