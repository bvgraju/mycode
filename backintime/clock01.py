#!/usr/bin/python3
import time # This is required to include time module

"""
Decoding a time tuple usually follows the formatting shown below.

Index Field Value
0 - 4-digit year
1 - Month 1 to 12
2 - Day 1 to 31
3 - Hour 0 to 23
4 - Minute 0 to 59
5 - Second 0 to 61 (60 or 61 are leap-seconds)
6 - Day of Week 0 to 6 (0 is Monday)
7 - Day of year 1 to 366 (Julian day)
8 - Daylight savings -1, 0, 1, -1 means library determines DST
"""

def main():
    ## Count the number of ticks from the epoch
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970: ", ticks)

    ## Show how we can convert ticks into a useful time tuple
    myTime = time.localtime(ticks) # pass ticks to localtime
    print("The local time tuple is: ", myTime)
    print("The local time tuple year is: ", myTime[0])
    print("The local time tuple month is: ", myTime[1])
    print("The local time tuple day is: ", myTime[2])
    print("The local time tuple hour is: ", myTime[3])
    print("The local time tuple minute is: ", myTime[4])
    print("The local time tuple second is: ", myTime[5])
    print("The local time tuple week is: ", myTime[6])
    print("The local time tuple year is: ", myTime[7])
    print("The local time tuple daylight savings is: ", myTime[8])

    for x in range(10):
        print('This program will end in...', x)
        time.sleep(5)

if __name__ == "__main__":
    main()

