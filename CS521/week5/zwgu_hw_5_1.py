"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Dec 8 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

•	takes as input from the user an English sentence
•	calls the function vc_counter() that:
	o	takes a string argument 
	o	counts the number of vowels and consonants in the string
	o	returns a dictionary of the counts, using the keys total_vowels and total_consonants
•	Uses the return from vc_counter() to print the total vowels and consonants with appropriate descriptions.

"""
import string

#dictionary
my_dict = {
	'total_vowels' : 0,
	'total_consonants' : 0,
	}


def vc_counter(user_string):
	#remove all the punctuation
	user_string = user_string.translate(str.maketrans('', '', string.punctuation))
	#remove all the space
	user_string = user_string.replace(" ", "")

	#check the number of vowels and add +1 to the dictionary
	for char in user_string :
		if char in ['a','e','i','o','u','A','E','I','O','U']:
			my_dict['total_vowels'] = my_dict.get('total_vowels') + 1 
		else:
			my_dict['total_consonants'] = my_dict.get('total_consonants') + 1 

	#return the result in complete sentece
	return('Total # of vowels in sentence: {}\nTotal # of consonants in sentence: {}'.format(my_dict.get('total_vowels'), my_dict.get('total_consonants')))

#start here
user_in = input('Enter an English sentence: ')
print(vc_counter(user_in))
