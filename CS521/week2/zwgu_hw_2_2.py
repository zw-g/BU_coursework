"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #2
Description of Problem (just a 1-2 line summary!):
Prompt user for input and then print that input as a string, an integer, and a floating-point value
and explain at then of the program why some input works and some does not
"""

#ask for input
user = input("please enter your input: ")

#print as a string, an integer, and a floating-point
print(str(user))
print(int(user))
print(float(user))

"""
Answer:
only enters integer will not bring up any error
float will cause and error becasue it can't be set to int
str will have error becasue it could not be set to int and float
"""