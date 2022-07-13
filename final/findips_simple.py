#!/usr/bin/env python3

# import csv

""" This program has 
      picks from the list the IP addresses
      Rules to consider a string as an IP address are,
        a) should be a string
        b) should have three dots
        c) all four elements are numbers
"""

""" Define a list with some strings that are ip addresses, 
    numbers, and strings that are not numbers 
"""

# with open('infile.csv', newline='') as infile:
#    reader = csv.reader(infile)
#    inlist = list(reader)

# print(inlist)


inlist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print ("Initial List was, \n", inlist) # First print the original list

realIPs = []  # Define an empty list for real IP addressed

for ip in inlist:  # Loop the original list
    if ( type(ip) == str ): # Ignpre if item is not a string
       breakIP = str(ip).split(".") # split with . seperator into list
       if ( len(breakIP) == 4 ) and all(item.isdigit() for item in breakIP):  # check if there are four elements and are numbers  
            realIPs.append(ip)
print("\nIdentified IP addresses are, \n", realIPs)
