"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Dec 8 2020
Homework Problem #2
Description of Problem (just a 1-2 line summary!):

•	takes as input from the user a date and time (24-hour clock) as "MM/DD/YYYY HH:mm:SS"
	o	Assume that everything must be provided with leading zeros
•	calls the function is_ validate_datetime () that:
	o	takes a string argument
	o	validates that the string has all the elements to be a valid date and time
	o	returns 2 values:
			Boolean true if valid or false if invalid date/time
			None if valid or an error message string if invalid
•	If the input string is returned from the function as invalid, print the returned error message.
•	If the input string is returned from the function as valid, use input string to print following:
	o	MM/DD/YYYY
	o	HR:MIN:SEC
	o	MM/YYYY
	o	Whether the time is “AM” or “PM”


"""

error_dict = {
	1 : 'error on date, format check \'/\' you should only have two',
	2 : 'error on input, format there should only be one (speace) in between date and time',
	3 : 'error on time, format check \':\' you should only have two',
	4 : 'error on month, there can be only 1-12 months in a year',
	5 : 'error on day, there can be only 1-31 days in a months',
	6 : 'error on year, the year must be 4 #\'s',
	7 : 'error on hr, the time hr can only be in between 0-23',
	8 : 'error on min, the time min can only be in between 0-59',
	9 : 'error on sec, the time sec can only be in between 0-59',
	}

def result(user_string):
	user_string = user_string.strip()
	user_string = user_string.split()
	date = user_string[0].split('/')
	time = user_string[1].split(':')

	print('MM/DD/YYYY is ' + user_string[0])
	print('HR:MIN:SEC is ' + user_string[1])
	print('MM/YYYY is {}/{}'.format(date[0], date[2]))
	if (int(time[0]) >= 12):
		print('The time is PM')
	else:
		print('The time is AM')


'''
error code:
1 = error on date format missing '/'
2 = error on input format missing (speace) in between date and time
3 = error on time format missing ':'
4 = there can be only 1-12 months in a year.
5 = there can be only 1-31 days in a months.
6 = the year must be 4 #'s.
7 = the time hr can only be in between 0-24
8 = the time min can only be in between 0-59
9 = the time sec can only be in between 0-59
no error code = perfect
'''
def is_validate_datetime(user_string):

	#pre set value
	count_one = count_two = count_three = 0
	user_string = user_string.strip()
	error_code_list = []

	#check error code for 1,2,3
	for elements in user_string: 
		if elements == '/':
			count_one = count_one + 1
		if elements == ' ':
			count_two = count_two + 1
		if elements == ':':
			count_three = count_three + 1

	if count_one != 2:
		error_code_list.append(1)
	if count_two != 1:
		error_code_list.append(2)
	if count_three != 2:
		error_code_list.append(3)
	
	#pre setup
	user_string = user_string.split()
	date = user_string[0].split('/')
	time = user_string[1].split(':')
	#print(user_string)
	#print(date)
	#print(time)
	#print(int(date[0]))

	#check error code for 4,5,6,7,8,9		
	if int(date[0]) > 12 or int(date[0]) < 1:
		error_code_list.append(4)
	if int(date[1]) > 31 or int(date[1]) < 1:
		error_code_list.append(5)
	if len(date[2]) != 4:
		error_code_list.append(6)
	if int(time[0]) > 23 or int(time[0]) < 0:
		error_code_list.append(7)
	if int(time[1]) > 59 or int(time[0]) < 0:
		error_code_list.append(8)
	if int(time[2]) > 59 or int(time[2]) < 0:
		error_code_list.append(9)

	#if there is any error code, else return True
	if len(error_code_list) == 0:
		#print('good')
		return True
	else:
		print ('Invalid: please enter a date time as MM/DD/YYYY HR:MIN:SEC')
		#print out all the posible error message
		for elements in error_code_list:
			print(error_dict.get(elements))
		return False

#start here
user_in = input('Enter a date time (MM/DD/YYYY HR:MIN:SEC): ')

if is_validate_datetime(user_in):
	result(user_in)
