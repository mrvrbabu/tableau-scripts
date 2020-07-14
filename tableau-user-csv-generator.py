#!/usr/local/bin/python3
# Title           : tableau-user-csv-generator.py
# Description     : This python script will generate a tableau user import compatible csv file
# Author          : Ramesh Babu
# Date            : 13 July 2020
# Version         : 1.0
# Usage           : python tableau-user-csv-generator.py
# Notes           : If you wish this script should run on another server, then make sure,
#                   you have changed the variables as mentioned below.
# Python_Version  : python >= 3.6
# Software	      : None
# Prerequesits	  : csv module (pip install csv), provide email id of a single user that will imported as csv file
#==============================================================================
''' Run the script
-----------------------------------------------------------------------------------------------'''

import os
import csv


def email_splitter(username):                                         # Generate firstname, lastname from email id Ex: - ramesh.babu@example.com
    fnamelastname = username.split('@')[0]
    return fnamelastname


def main():
    username = input("Please input the tableau user email : ")        # Provide tableau user email id
    fullname = email_splitter(username)
    filename = fullname.replace(".", "_")                             # Replace '.' with '_' that will be used to create meaningful filename
    fullname = fullname.title()                                       # Capitalize first character of firstname and lastname to uppercase
    fullname = fullname.replace(".", " ")                             # Replace '.' with ' ' which will be the firstname and lastname in tableau
    namesplit = fullname.split()                                      # Split and store firstname and lastname to create password from firstanme.
    fname = namesplit[0]

    with open(filename + ".csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, fname + "@123", fullname, "Viewer", "None", "no", username])    # Create a csv file in the format of username, password, fname lastname, tableau license, None, no, email id


if __name__ == "__main__":
    main()
