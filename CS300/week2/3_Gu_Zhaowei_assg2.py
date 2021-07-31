'''
Zhaowei Gu
CS 300

Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration in months was entered by user in response to a prompt
4. (Error check): EITHER the user entered an integer between 1 and 100 for duration after being given up to two chances OR the application quit after suggesting a re-run.
5. (Action Recommended): EITHER how_long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few 
   sessions" is on the console OR the following is on the console:
   "Come back in a couple of months if this persists".
'''

answer = input("Thank you for using Eliza300, a fun therapy program.\nPlease state your complaint:\n") 
answer = input("How many months has it been that have you exprienced \'"+str(answer)+"\'?\n")
if int(answer) >= 1 and int(answer) <= 100: # using and/or
	if int(answer) > 2:
		print(answer+" months is too much time to go without help! Let's schedule a few sessions.")
	else:
		print("Come back in a couple of months if this persists")
else:
	answer = input("Please try one more time to enter duration in months less than 100\n")
	if int(answer) >= 1 and int(answer) <= 100: # using and/or
		if int(answer) > 2:
			print(answer+" months is too much time to go without help! Let's schedule a few sessions.")
		else:
			print("Come back in a couple of months if this persists")
	else:
		print("Sorry, try running Eliza again")
import sys
sys.exit()

'''
outcome(s):
#1
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I'm sad
How many months has it been that have you exprienced 'I'm sad'?
333
Please try one more time to enter duration in months less than 100
33
33 months is too much time to go without help! Let's schedule a few sessions.

#2
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I'm sad
How many months has it been that have you exprienced 'I'm sad'?
555
Please try one more time to enter duration in months less than 100
666
Sorry, try running Eliza again

#3
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I'm sad
How many months has it been that have you exprienced 'I'm sad'?
333
Please try one more time to enter duration in months less than 100
99
99 months is too much time to go without help! Let's schedule a few sessions.

#4
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I'm sad
How many months has it been that have you exprienced 'I'm sad'?
333
Please try one more time to enter duration in months less than 100
2
Come back in a couple of months if this persists
'''
