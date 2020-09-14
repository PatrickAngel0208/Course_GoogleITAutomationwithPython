#!/usr/bin/env python3
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string,max_width)) #wrap the given string with the max_width(this produces a list), join every part of the list with asked format

print(wrap("HolaComoEstas", 4))

'''

INPUT: "HolaComoEstas", 4

OUTPUT: 
Hola
Como
Esta
s

'''