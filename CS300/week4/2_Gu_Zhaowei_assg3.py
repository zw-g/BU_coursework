# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 2

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing', 
        'not working on weekends', 'spending two hours a day with friends']

'''
Precondition: possible_actions is the list defined above

Postconditions:

1. (Welcome): A welcome message is on the console

2. (user_complaint): user_complaint is the user's response to
"Please describe your emotional complaint--in one punctuation-free line: "

3. (how_long): how_long is the user's string response to
"How many months (between 1 and 99) have you experienced ...?"

4. (Month validity): EITHER how_long has the requested form
OR this terminated AND "Sorry, illegal input. Eliza is quitting; run Eliza again."
is on the console

5. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_action are on separate lines
on the console, each preceded by "Try ".
'''

print("Thank you for using ELliza300, a fun therapy program.")
strans = input("Please describe your emotional complaint--in one punctuation-free line:\n")
numans = input("How many months (between 1 and 99) have you experienced ...?"+strans+"\'?\n")
if numans.isnumeric() and int(numans) >= 1 and int(numans) <= 99:
	if int(numans) < 3:
		numans = 3 - int(numans)
		print("Please return in "+str(numans)+" months")
	else:
		print(numans+" months is significant. Sorry to hear it")
		for element in possible_actions:
			print("Try "+element)
else:
	print("Sorry, illegal input. Eliza is quitting; run Eliza again.")

import sys
sys.exit()

'''
OUTPUT
============ RESTART: /Users/zhaoweigu/Desktop/2_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I can't sleep at night
How many months (between 1 and 99) have you experienced ...?I can't sleep at night'?
155
Sorry, illegal input. Eliza is quitting; run Eliza again.
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/2_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I can't sleep at night
How many months (between 1 and 99) have you experienced ...?I can't sleep at night'?
7
7 months is significant. Sorry to hear it
Try taking up yoga
Try sleeping eight hours a night
Try relaxing
Try not working on weekends
Try spending two hours a day with friends
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/2_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I can't sleep at night
How many months (between 1 and 99) have you experienced ...?I can't sleep at night'?
2
Please return in 1 months
'''
