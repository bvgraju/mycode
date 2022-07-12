#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

ipchk = input("Apply and IP address: ")

# a string tests as 
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:   # note that as ipchk is not empty it evaluates as True Bool
    print("Looks like the IP address was set: " + ipchk)
else: 
    print("you did not provide input.")
