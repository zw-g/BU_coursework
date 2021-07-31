"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #7
Description of Problem (just a 1-2 line summary!):
Rewrite this following ‘for loop’ as a ‘while loop’:
for i in range(1, X + 1):
	if X % i == 0:
		print(i)

since X is not defined to I set it to a random number in between 1-100
"""

#set X to random number
import random
X = random.randint(1, 100)


#while loop starts
i = 0
while i < X:
	i += 1
	if X % 1 == 0:
		print(i)
