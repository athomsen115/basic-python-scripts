#!/usr/bin/env python3.8

message = input("Enter a message: ")
count = input("Enter a number of times to repeat the message: ")

if count:
    count = int(count)
else:
    count = 1
def repeat_message(message, count):
    while count > 0:
        print(message)
        count -= 1

repeat_message(message, count)
