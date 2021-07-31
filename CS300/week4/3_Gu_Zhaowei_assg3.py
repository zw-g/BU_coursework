# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 2

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing', 
        'not working on weekends', 'spending two hours a day with friends']
list = []

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

5. (Advice): EITHER how_long >= 3
OR "Please return in * months" is on the console where * is 3 - how_long

6. (actions_not_taken): actions_not_taken consists of the actions (elements) in
possible_actions that the user answered 'n' to when questioned "Have you tried..."

7. (Summarized): Eliza300 recommended that the user take the actions in
actions_not_taken
'''


print("Thank you for using ELliza300, a fun therapy program.")
strans = input("Please describe your emotional complaint--in one punctuation-free line:\n")
numans = input("How many months have you experienced \'"+strans+"\'?\n")
if numans.isnumeric() and int(numans) >= 1 and int(numans) <= 99:
	if int(numans) < 3:
		numans = 3 - int(numans)
		print("Please return in "+str(numans)+" months")
	else:
		print(numans+" months is significant. Sorry to hear it")
		for element in possible_actions:
			ans = input("Have you tried..."+element+"? please answer y or n:\n")
			if ans in ['n', 'N', 'no', 'No', 'NO']:
				list.append(element)
		print("After careful analysis:), here is Eliza300's advice:")
		for element in list:
			print(element)
else:
	print("Sorry, illegal input. Eliza is quitting; run Eliza again.")

import sys
sys.exit()

'''
OUTPUT
============ RESTART: /Users/zhaoweigu/Desktop/3_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I sleep though lunches
How many months have you experienced 'I sleep though lunches'?
5
5 months is significant. Sorry to hear it
Have you tried...taking up yoga? please answer y or n:
n
Have you tried...sleeping eight hours a night? please answer y or n:
y
Have you tried...relaxing? please answer y or n:
n
Have you tried...not working on weekends? please answer y or n:
y
Have you tried...spending two hours a day with friends? please answer y or n:
n
After careful analysis:), here is Eliza300's advice:
taking up yoga
relaxing
spending two hours a day with friends
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/3_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I sleep though lunches
How many months have you experienced 'I sleep though lunches'?
155
Sorry, illegal input. Eliza is quitting; run Eliza again.
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/3_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I sleep though lunches
How many months have you experienced 'I sleep though lunches'?
99
99 months is significant. Sorry to hear it
Have you tried...taking up yoga? please answer y or n:
y
Have you tried...sleeping eight hours a night? please answer y or n:
y
Have you tried...relaxing? please answer y or n:
y
Have you tried...not working on weekends? please answer y or n:
y
Have you tried...spending two hours a day with friends? please answer y or n:
y
After careful analysis:), here is Eliza300's advice:
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/3_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I sleep though lunches
How many months have you experienced 'I sleep though lunches'?
3
3 months is significant. Sorry to hear it
Have you tried...taking up yoga? please answer y or n:
n
Have you tried...sleeping eight hours a night? please answer y or n:
n
Have you tried...relaxing? please answer y or n:
n
Have you tried...not working on weekends? please answer y or n:
n
Have you tried...spending two hours a day with friends? please answer y or n:
n
After careful analysis:), here is Eliza300's advice:
taking up yoga
sleeping eight hours a night
relaxing
not working on weekends
spending two hours a day with friends
>>> 
============ RESTART: /Users/zhaoweigu/Desktop/3_Gu_Zhaowei_assg3.py ===========
Thank you for using ELliza300, a fun therapy program.
Please describe your emotional complaint--in one punctuation-free line:
I sleep though lunches
How many months have you experienced 'I sleep though lunches'?
2
Please return in 1 months
'''
