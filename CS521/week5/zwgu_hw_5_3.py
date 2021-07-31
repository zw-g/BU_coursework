"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Dec 8 2020
Homework Problem #3
Description of Problem (just a 1-2 line summary!):

Prompts the user for three numbers in one request.  
Be sure to specify the “delimiter” by which a user enters those three numbers. 

Divides the first number by the second number and add that result to the third number.

Prints output that shows in one line the formula applied and the result of the calculation.

Validate input by: 
•	Checking the user entered 3 values
•	Appropriately checking for the following errors: ValueError and ZeroDivisionError.  
•	Printing descriptive error messages to the console if validation fails.
•	Remembering to have very granular testing blocks
"""

def three_value_check(user_in):
	user_in = user_in.strip()
	user_in = user_in.split()

	#see if there are 3 number being input
	if len(user_in) == 3:
		return True
	else:
		print ('Value Error need 3 numbers')
		return False

def value_error(user_in):
	user_in = user_in.strip()
	user_in = user_in.split()

	#see if all the number works
	try:
		a = float(user_in[0])
		b = float(user_in[1])
		c = float(user_in[2])
	except:
		#ValueError
		print ('Value Error input must be 3 numbers')
		return False
	else:
		return True

def zero_division_error(user_in):
	user_in = user_in.strip()
	user_in = user_in.split()

	#see if the math are allowing these numbers
	try:
		result = float(user_in[0]) / float(user_in[1])
	except:
		#ZeroDivisionError
		print ('Zero DivisionError, the 2nd number can\'t be 0')
		return False
	else:
		return True

#start here, use the __name__ == "__main__" so that we do not need to access this part when we need other functions
if __name__ == "__main__":
	#user input
	user_in = input('Please enter three numbers (23 43 56): ')

	#check if all the error are ok
	if three_value_check(user_in) and value_error(user_in) and zero_division_error(user_in):
		user_in = user_in.strip()
		user_in = user_in.split()

		#print (float(user_in[0]))

		#do the calculation
		result = (float(user_in[0]) / float(user_in[1])) + float(user_in[2])
		result = '{:,.2f}'.format(result)

		print('({}/{})+{} = {}'.format(user_in[0],user_in[1],user_in[2],result))
