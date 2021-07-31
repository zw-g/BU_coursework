"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Start with 2 constant lists. One with first names and another of last names. 

First validate that both lists are the same size and if not, exit with an error message. 

Use zip to create a dictionary with the keys as the last names and the values as the first 
names. Print the generated dictionary with an appropriate description.
"""

#2 constant lists
First_Names = ['Jane', 'John', 'Jack']
Last_Names = ['Doe', 'Deer', 'Black']

#validate that both lists are the same size and if not, exit with an error message
if (len(First_Names) == len(Last_Names)):
	#zipped = list(zip(Last_Names, First_Names))
	print ("First Names: {}".format(First_Names))
	print ("Last Names: {}".format(Last_Names))
	print (end="Name Dictionary: {")

	#logic zip two together to dictionary
	for la, fi in zip(Last_Names, First_Names):
		print (end="\'%s\': \'%s\'" %(la, fi))
		#print(fi)
		if (fi == First_Names[-1]):
			print ("}")
		else:
			print (end=", ")
else:
	print("ERROR the lists are not the same size")
