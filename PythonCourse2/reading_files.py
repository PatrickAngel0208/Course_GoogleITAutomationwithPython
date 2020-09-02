#!/usr/bin/env python3
def CodelandUsernameValidation(strParam):

    if len(strParam) >= 4 and len(strParam) <= 25 and strParam[0].isalpha() and strParam[-1] != "_":
        strParam_status = True
    else:
        strParam_status = False
    return strParam_status

# keep this function call here 
print(CodelandUsernameValidation(input()))