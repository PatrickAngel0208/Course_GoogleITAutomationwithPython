#!/usr/bin/env python3

'''
The proposal is to build the required mix of resistors to generate a specific value, this mix will be generated from a database.
'''
import csv

with open("re_database.csv") as file:
    csv_f = csv.reader(file)
    for row in csv_f:
        print(row)


