"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Write a Python program that counts the number of 
odd numbers, 
even numbers, 
squares of an integer 
and cubes of an integer 
from 2 to 130 (inclusive). 

For example, 
9 is both odd and a square, 
8 is even and a cube. 
Use “constants” to set the beginning and ending of the range.

For output, print a title with the total range.
For Odd and Even, print the totals and the range of the numbers in scope.
For Squares and Cubes, print the totals and a list of the numbers that meet the criteria
Nothing printed should be hard coded.
"""

import math

#Constant
beginning = 2
ending = 130

#notice user
print ("Checking numbers form " + str(beginning) + " to " + str(ending))

#odd number
count = 0
outList = []
for x in range(beginning, ending+1, 1):
	if (x % 2 == 1):
		outList.append(x)
		count += 1
print ("Odd (" + str(count) + "): " + str(outList[0]) + "..." + str(outList[-1]))

#even number
count = 0
outList = []
for x in range(beginning, ending+1, 1):
	if (x % 2 == 0):
		outList.append(x)
		count += 1
print ("Even (" + str(count) + "): " + str(outList[0]) + "..." + str(outList[-1]))

#square number
count = 0
outList = []
for x in range(beginning, ending+1, 1):
	n = math.sqrt(x)
	if (n.is_integer()):
		outList.append(x)
		count += 1
print ("Square (" + str(count) + "): {}".format(outList))

#cube number
count = 0
outList = []
for x in range(beginning, ending+1, 1):
	if round(x ** (1 / 3)) ** 3 == x:
		outList.append(x)
		count += 1
print ("Cube (" + str(count) + "): {}".format(outList))
