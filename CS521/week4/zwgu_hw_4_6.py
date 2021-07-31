"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Create a program that:
•	prompts a user for a number
•	validates the number
•	re-prompts on error
•	converts the number to words using a dictionary
•	prints out the converted numbers as words

The program must only have one input command and work for any size positive or negative number.

Decimal point should be converted to ‘point’.
If the user enters commas, tell them to try again without the commas.

"""

def check (number):
	#see if there are commas in the user input
	bools = list(map(lambda char: char in ',', number))
	if any(bools):
		print ('Please try again without entering commas.')
		start ()
		return False

	#remove the . and -
	for char in '.':
		line = number.replace(char,'')
	for char in '-':
		line = line.replace(char,'')
	#see if is is a number, check logic
	if (line).isnumeric():
		if number[0] == '-':
			for n in range (1, len(number), 1):
				if number[n] == '-':
					#print (number[n])
					print ('\"' +number+ '\" is not a valid number. Please try again')
					start ()
					return False
			return True
		else:
			for n in range (1, len(number), 1):
				if number[n] == '-':
					#print (number[n])
					print ('\"' +number+ '\" is not a valid number. Please try again')
					start ()
					return False
			return True
	else:
		print ('\"' +number+ '\" is not a valid number. Please try again')
		start ()
		return False

def start ():
	#outprint
	number = input("Enter a number: ")

	#check the input
	if (check (number)):
		#print out the input using dictionary
		print (end='As Text: ')
		for n in range (len(number)):
			for key, value in my_dict.items():
				if number[n] == (str(key)):
					print (value,end=' ')
		print ()

#dictionary
my_dict = {
	'-':'Negative',
	'.':'Point',
	'1':'One',
	'2':'Two',
	'3':'Three',
	'4':'Four',
	'5':'Five',
	'6':'Six',
	'7':'Seven',
	'8':'Eight',
	'9':'Nine',
	'0':'Zero',
	}

start()
