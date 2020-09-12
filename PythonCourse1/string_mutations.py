#!/usr/bin/env python3

#This is the first method, where the string is sliced and joined it back.
'''
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:] 
    return new_string

print(mutate_string("CarlosAngel", 9, "E"))
'''

#This is the secong method, where the string is converted to a list and then change the value.

def mutate_string(string, position, character):
    list_from_string = list(string) #Convert string into a list
    list_from_string[position] = character #Update the character at the given position
    new_string = "".join(list_from_string) #Join the list with the new character
    return new_string

print(mutate_string("CarlosAngel", 9, "E"))