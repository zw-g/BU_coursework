"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #2
Description of Problem (just a 1-2 line summary!):

Set a constant with an odd length string.
Confirm in code that the string is of an odd length. 
Otherwise, print a relevant message for the user and end the program.
For a string of odd length, print each of the following in double quotes:
•	Print the entire string and its length.
•	Print the middle character.
•	Print the string up to but not including the middle character.
•	Print the string from immediately following the middle character to the end.
"""
import sys 

#constant
oddLengthString = "A man a plan a canal Panama"

length = len(oddLengthString)

if (length % 2 != 0):
	print("My " +str(length)+ " character string is: \"" +oddLengthString+ "\"")

	#get the middle information
	mid = (len(oddLengthString)-1)//2
	mid2 = (len(oddLengthString)+2)//2

	#print
	print("The middle character is : \"" +oddLengthString[mid:mid2]+ "\"")
	print("The 1st half of string is: \"" +oddLengthString[0:mid]+ "\"")
	print("The 2nd half of string is: \"" +oddLengthString[mid2:-1]+ "\"")
else:
	#if the input are is not constant
	print("The string length is not even")
	sys.exit()
