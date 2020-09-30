#!/usr/bin/env python3

import re
import csv

def contains_domain(address, domain):
    domain = r'[\w\.-]+@'+domain+'$' #create pattern of the domain
    if re.match(domain,address): 
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r'' + old_domain + '$' #create pattern. It needs to have the domain, and be in the final part, if not it doesn't match. Ex: as@edu.mx -> Matches. ash@edu.mx.mv -> not match.
    address = re.sub(old_domain_pattern, new_domain, address) #replace the old domain with the new one.
    return address

def main():
    old_domain, new_domain = 'abc.edu', 'xyz.edu'

    csv_file_location = '/home/carlosangel/Documents/GoogleAutomationCourse/PythonCourse1/user_emails.csv'
    report_file = '/home/carlosangel/Documents/GoogleAutomationCourse/PythonCourse1/updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]] #this creates a new list, without headers and names, only emails. -> user_data_list[1:] doesn't take the row 0 (headers). -> data[1].strip doesn't take the column 0 (where the names are), so the for only itarates with the emails

    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address) #create a list which will have all the emails that have an old email
            replaced_email = replace_domain(email_address,old_domain,new_domain)
            new_domain_email_list.append(replaced_email)  #create a list with all the emails with the domain updated.
    

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    

    for user in user_data_list[1:]: #go through every row [name_user, email_user]
        for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list): #create a touple of with the new and old email, and they are assigned to the variable old_domain and new_domain
            if user[email_index] == ' ' + old_domain: #this updates the user_data_list
                user[email_index] = ' ' + new_domain
    #print(user_data_list)
    f.close()

    with open(report_file, 'w+') as output_file: #this writes the new emails in the new csv file
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()