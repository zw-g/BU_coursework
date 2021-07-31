"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Using my_dict = {a':15, 'c':18, 'b':20}, write a program to:
a.	print all the keys.
b.	print all the values.
c.	print all the keys and values pairs.
d.	print all the keys and values pairs in order of key.
e.	print all the keys and values pairs in order of value.
* Ordering may be ascending or descending

"""
#from collections import OrderedDict

my_dict = {
	'a':15, 
	'c':18, 
	'b':20
	}

#Key
print('a. Keys: {}'.format(list(my_dict.keys())))

#Values
instant = list(my_dict.values())
print (end="b. Values: ")
print(*instant, sep=", ")

#Key value pairs
print (end="c. Key value pairs: ")
for x, y in my_dict.items():
	#print (x)
	#print (list(my_dict.keys())[-1])
	if x != list(my_dict.keys())[-1]:
		print (end="{}: {}, ".format(x, y))
	else:
		print ("{}: {}".format(x, y))

#Key value pairs ordered by key
instant = [list(sorted(my_dict.items(), key=lambda x: x[0]))]
print (end="d. Key value pairs ordered by key: ")
print(*instant)

'''
#Key value pairs ordered by value
instant = sorted(my_dict.items(), key=lambda x: x[1])
print (end="e. Key value pairs ordered by value: ")
print(type(instant))
print(instant)
'''

#Key value pairs ordered by value
print (end="e. Key value pairs ordered by value: ")
instant = dict(sorted(my_dict.items(), key=lambda item: item[1]))
for x, y in instant.items():
	if x != list(instant.keys())[-1]:
		print (end="{}: {}, ".format(x, y))
	else:
		print ("{}: {}".format(x, y))
