#!/usr/bin/env python3.8

from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)} UTC")

#Wait for user to stop timer
input("Press enter to stop time ")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)} UTC")
print(f"Total time: {difference} seconds")
