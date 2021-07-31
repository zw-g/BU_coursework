# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 1

possible_actions = ['taking up yoga.', 'sleeping eight hours a night.', 'relaxing.', 
        'not working on weekends.', 'spending two hours a day with friends.']

'''
Precondition: possible_actions is the list defined above

Postconditions:
1. (Welcome): A welcome message is on the console
2. (user_complaint): user_complaint is the user's response to a prompt for the
user's complaint
3. (how_long): how_long is the user's string response to "How many months have
you experienced ...?" AND Eliza300 sympathized, mentioning the duration
4. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_action are on separate lines
on the console, each preceded by "Try ". 
'''

print("Thank you for using ELliza300, a fun therapy program.")
strans = input("Please describe your emotional complaint--in one punctuation-free line:\n")
numans = input("How many months have you experienced \'"+strans+"\'?\n")
if numans.isnumeric():
	if int(numans) < 3:
		numans = 3 - int(numans)
		print("Please return in "+str(numans)+" months")
	else:
		print(numans+" months is significant. Sorry to hear it")
		for element in possible_actions:
			print("Try "+element)

import sys
sys.exit()
