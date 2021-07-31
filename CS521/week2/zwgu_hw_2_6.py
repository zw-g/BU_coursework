"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #6
Description of Problem (just a 1-2 line summary!):
calculated and prints all the leap years from 1900 to 2020 (inclusive)
using a ‘for loop’ and then using a ‘while loop’

logic:
if year is not divisible by 4 then it is a common year
else if year is not divisible by 100 then it is a leap year
else if year is not divisible by 400 then it is a common year
else it is a leap year
"""

print("for loop:")
for x in range(1900, 2021, 1):
	#logic
	if x%4 != 0:
		continue
	elif x%100 != 0:
		print(x)
	elif x%400 != 0:
		continue
	else:
		print(x)

print("\nwhile loop:")
i = 1899
while i < 2020:
	i += 1
	#logic
	if i%4 != 0:
		continue
	elif i%100 != 0:
		print(i)
	elif i%400 != 0:
		continue
	else:
		print(i)
