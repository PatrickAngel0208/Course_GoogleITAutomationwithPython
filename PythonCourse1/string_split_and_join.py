#!/usr/bin/env python3

def split_and_join(line):
    line_ls = line.split() #create a list from the given string
    new_string = "-".join(line_ls) #join evey element of the list with '-' between every element
    return new_string

print(split_and_join("this is a string"))

'''

IN: "this is a string"
OUT: this-is-a-string

'''