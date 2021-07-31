"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):
in this code I will have to ask for a number from the user, then, 
add 2, multiply by 3, subtract 6, and divide by 3
finaly I have to check using an IF statement so that the user input
and the calculation are the same.
"""
#ask for user input
user = input("please enter a number: ")
number = float(user)

#do the calculation
number = ((number+2)*3-6)/3

#check and print
if number == int(user):
	print("the input is equal to the result from the calcualtion they are both: " + str(number))
