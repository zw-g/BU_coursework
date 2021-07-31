"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Given a constant list of integers, write Python code to generate 
a new list with same number of elements as the original list such 
that each integer in the new list is the sum of its nearest 
neighbors and itself from the original list. Print both lists with descriptions. 
"""

#constant list of integers
inList = [10, 20, 30, 40, 50]
outList = []

#logic append
for i in range (0, len(inList), 1):
	if i == 0:
		outList.append(inList[i] + inList[i+1])
	elif inList[i] == inList[-1]:
		outList.append(inList[i] + inList[i-1])
	else:
		outList.append(inList[i] + inList[i-1] + inList[i+1])

#print
print ("Input List: {}\nResult List: {}".format(inList, outList))
