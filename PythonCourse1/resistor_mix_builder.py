#!/usr/bin/env python3

'''
The proposal is to build the required mix of resistors to generate a specific value, this mix will be generated from a database.
'''
import csv
import re

def ask_value():
    state = True
    while state == True: #Ask to user the value while the input is not in the format
        resistor_value = input("What value do you want? (H = ohms, K = KiloOhms, M = MegaOmhs): ")
        if re.search(r"[HKM]$",resistor_value): #Check if the input ends with KM
            state = False
    return resistor_value

def check_resistor_value(resistor_value):

    resistor_value_status = False
    resistor_value_quantity = 0

    with open("resistors_database.csv") as file:
        csv_f = csv.DictReader(file)
        #next(csv_f, None) #Skip the header of CSV file
        res_list = [] #make a list of the dictionaries
        for data in csv_f:
            res_list.append(dict(data)) 
        
        for res_dict in res_list: #go through every dictionary of th e list
            if res_dict["value"] == resistor_value: #check if the asked value is in the data base
                resistor_value_status = True
                resistor_value_quantity = res_dict["quantity"]
    
    return resistor_value_status, resistor_value_quantity



resistor_value_status, resistor_value_quantity = check_resistor_value(ask_value())

if resistor_value_status and resistor_value_quantity != '0':
    print("Hey! Friend you have {} reistors of the asked value.".format(resistor_value_quantity))
else:
    None