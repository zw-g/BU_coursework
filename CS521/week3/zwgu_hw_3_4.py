"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #4
Description of Problem (just a 1-2 line summary!):

Write a program that prompts the user to enter a three-digit whole number 
such that the digits are in ascending order and without duplicates.

Valid examples: 123 and 489 
Invalid examples: 133 and 174

The program loops and re-prompts the user until a correct value is entered. 
 Make sure to check whether the user entered the correct data type.

"""

#ask for input and start to check
def start():
	userInput = input("Please enter a 3-digit integer: ")
	intCheck(userInput)

#check the int
def intCheck(n):
	try:
		val = int(n)
		#print("Number Accepted1")
		wholCheck(n)
	except ValueError:
		print("This is not an integer. Please re-enter.")
		start()
		
#check to see if the numner is a whole number
def wholCheck(n):
	if(int(n) >= 0):
		#print("Number Accepted")
		lengthCheck(n)
	else:
		print("This is not a whole number. Please re-enter.")
		start()

#check the length 
def lengthCheck(n):
	if(len(n) == 3):
		#print("Number Accepted2")
		dupCheck(n)
	else:
		print("You did not enter a 3-digit number.")
		start()

#check the duplication
def dupCheck(n):
	if((n[0] != n[1]) and (n[0] != n[2]) and (n[1] != n[2])):
		#print("Number Accepted3")
		ascCheck(n)
	else:
		print("Your number contains duplication.")
		start()

#check to see if it is in accending order
def ascCheck(n):
	if((n[0] < n[1]) and (n[1] < n[2])):
		print("Number Accepted")
	else:
		print("The digits are not in ascending order.")
		start()


#start the application
start()
