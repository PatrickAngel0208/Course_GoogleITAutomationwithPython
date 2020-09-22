#!/usr/bin/env python3

'''
The proposal is to build the required mix of resistors to generate a specific value, this mix will be generated from a database.
'''
import csv
import re

def ask_value():
    state = True
    while state == True: #Ask to user the value while the input is not in the format
        resistor_value = input("What value do you want? (noLetter = ohms, K = KiloOhms, M = MegaOmhs): ")
        if re.search(r"[KM]$",resistor_value): #Check if the input ends with KM
            state = False
    return resistor_value

def check_resistor_value(resistor_value):
    with open("resistors_database.csv") as file:
        csv_f = csv.reader(file)
        next(csv_f, None) #Skip the header of CSV file
        for row in csv_f:
            if resistor_value == row[0]:
                resistor_value_status = True
            else:
                resistor_value_status = False
    return resistor_value_status


check_resistor_value(ask_value())