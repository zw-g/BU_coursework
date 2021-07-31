'''
Zhaowei Gu
CS 300

Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration was entered by user in response to a prompt
4. (Action Recommended): EITHER how long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few sessions"
   is on the console
   OR the following is on the console:
   "Come back in a couple of months if this persists".
'''



answer = input("Thank you for using Eliza300, a fun therapy program.\nPlease state your complaint:\n") 
answer = input("How many months has it been that have you exprienced \'"+str(answer)+"\'?\n")
if int(answer) > 2:
	print(answer+" months is too much time to go without help! Let's schedule a few sessions.")
else:
	print("Come back in a couple of months if this persists")
import sys
sys.exit()

'''
outcome(s):
#1
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I feel happy all day except for 2:30 to 3:00 pm.
How many months has it been that have you exprienced 'I feel happy all day except for 2:30 to 3:00 pm.'?
5
5 months is too much time to go without help! Let's schedule a few sessions.

#2
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
I feel happy all day except for 2:30 to 3:00 pm.
How many months has it been that have you exprienced 'I feel happy all day except for 2:30 to 3:00 pm.'?
2
Come back in a couple of months if this persists
'''
