import csv
import pandas as pd

with open('123.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    column1 = [row[2]for row in reader]
    print(column1)