#!/usr/bin/env python3

"""This program has 
   different aspects of list processin
"""

# first create the list with IP, port and state
my_list = [ "192.168.0.5", 5060, "UP" ]

# print the ip
print("The first item in the list (IP): " + my_list[0] )

# print the port. Note that needs to be converted to string
print("The second item in the list (port): " + str(my_list[1]) )

# print the state
print("The last item in the list (state): " + my_list[2] )

#define iplist
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display only ip addresses
print("IP Addresses in IPList: ", iplist[3], iplist[4])

#another way
realIp = iplist[3:5]
print("IPs are: ",realIp[0], realIp[1])

#third way
import ipaddress
print("IPs are,")
for ip in iplist:
    try ipaddress.ip_address(ip):
      print(ip)
