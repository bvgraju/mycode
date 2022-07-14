#!/usr/bin/env python3

import csv

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

def main():

    with open('infile.csv', newline='') as infile:
        reader = csv.reader(infile)
        inlist = list(reader)

    print ("\n\nInitial List was, \n", inlist) # First print the original list

    IPsOut = []

    for EachLine in inlist:  # Loop each line
        IPsInLine = [] # for storing IPs in each line

        for txt in EachLine:    # loop each element seperated by comma in a line

            if ( type(txt) == str ): # Ignpre if item is not a string
                SplitTxt = str(txt.strip()).split(".") # split with . seperator into list
                if ( len(SplitTxt) == 4 ) and all(item.isdigit() for item in SplitTxt):  
                # check if there are four elements and are all numbers  
                    IPsInLine.append(txt.strip() )
    
        IPsOut.append(IPsInLine)

    print("\n\n Identified IPs are: \n", IPsOut)

    """ Now write list to the file
    """
    # writing the data into the file
    with open("IPOut.csv", "w") as file:
        write = csv.writer(file)
        write.writerows(IPsOut)

if __name__ == "__main__":
    main()
