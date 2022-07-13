#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

print("\n First Item: ", configlist[1])
print("\n Last Item: ", configlist[-1])

## Always close your file
configfile.close()
