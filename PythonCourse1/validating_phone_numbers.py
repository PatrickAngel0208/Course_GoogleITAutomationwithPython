#!/usr/bin/env python3

import re

for i in range(int(input())):
    pho_number = input()
    match = re.search(r'[789]\d{9}$',pho_number)
    if match:
        print(True)
    else:
        print(False)

'''

IN:
2
9587456281
1252478965

OUT:
YES
NO


'''