"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #3
Description of Problem (just a 1-2 line summary!):

Write a program that prompts the user for a sentence and calculates 
the number of uppercase letters, lowercase letters, digits, and punctuation. 
Output the results neatly formatted and labeled in columns. 
Use .format()
"""
import string 

#get the in put
user = input("please enter a sentence: \n")

#output constant
output = "# Upper   # Lower   # Digits  # Punct.\n--------  --------  --------  --------\n   {}         {}        {}         {}    "

#initial costant
length = len(user)
upper = 0
lower = 0
digits = 0
punct = 0

#logic
for x in user:
	if (x.isupper()) == True:
		upper += 1
	elif (x.islower()) == True:
		lower += 1
	elif (x.isnumeric()) == True:
		digits += 1
	elif x in string.punctuation:
		punct += 1
	else:
		break

#　print the result using format method
print(output.format(upper, lower, digits, punct))
