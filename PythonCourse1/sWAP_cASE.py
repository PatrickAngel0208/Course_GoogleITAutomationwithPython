#!/usr/bin/env python3

def swap_case(s):
    string = "" 
    for i in s: #iterate the input string
        if i.islower() == True: #check if the letter is lower case or not
            string += i.upper()
        else:
            string += i.lower()

    return string

print(swap_case("Today will be a great Day"))