"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #3
Description of Problem (just a 1-2 line summary!):
ask for int (n)
do math n+n*n+n*n*n+n*n*n*n= ?
print the equation and the result
"""

#input
user = input("please enter an integer(n): ")
n = int(user)

#math
n = n+n*n+n*n*n+n*n*n*n

#print
print (user+" + "+user+" * "+user+" + "+user+" * "+user+" * "+user+" + "+user+" * "+user+" * "+user+" * "+user+" = "+str(n))
