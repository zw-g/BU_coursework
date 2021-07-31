'''
Zhaowei Gu
CS 300

Postconditions

1 (Welcome): A welcome message is on the console

2 (Complaint): A complaint was entered by the user in response to a prompt

AND Eliza has responded "I am sorry to hear you report <the complaint entered by the user>"

'''


answer = input("Thank you for using Eliza300, a fun therapy program.\nPlease state your emotional complaint then hit ENTER:\n") 
print("I am sorry to hear you report \""+str(answer)+"\"!")
import sys
sys.exit()

'''
outcome(s):
Thank you for using Eliza300, a fun therapy program.
Please state your emotional complaint then hit ENTER:
I have been depressed for six months
I am sorry to hear you report "I have been depressed for six months"!
'''
