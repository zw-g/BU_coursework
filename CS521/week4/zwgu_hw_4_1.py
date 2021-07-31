"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Given a constant list of integers in the range 1 to 10 inclusive, use list comprehension (no explicit loops) to:
•	find the sum of the even integers in list L.
•	find the sum of the odd integers in list L.
"""
#constant list
L = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

#use list comprehension to find the sum of even
sum_even = sum([n for n in L if n%2 == 0])

#use list comprehension to find the sum of odd
sum_odd = sum([n for n in L if n%2 == 1])

#print
print(end="Evaluating the numbers in: ")
print (*L, sep=", ")

#print ans
print ("Even: {}\nOdd: {}".format(sum_even, sum_odd))
