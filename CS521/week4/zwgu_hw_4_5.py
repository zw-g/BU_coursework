"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 27 2020
Homework Problem #1
Description of Problem (just a 1-2 line summary!):

Write the following python program. 

Assign to a constant variable an English sentence of at least 15 characters.

Print the starting sentence

Create a dictionary with the letters as keys and frequency counts as values.
Print the dictionary.

Create a string of the most common letter(s) in the sentence. In the case of a tie for the 
most common letter, the string will have all of them
Print the string and the number of times the letter(s) appeared in the sentence

Create a list of the unique letters, with each letter being the repeated number of times it 
appears in the string. Then print this list as one element per line (a histogram).
"""
#sort the string to dictionary
def CountFrequency(my_list): 
    # Creating an empty dictionary  
    freq = {}
    my_list = my_list.replace(" ", "")
    print(end='{')
    for items in my_list:
        freq[items] = my_list.count(items) 
    freq = dict(sorted(freq.items(), key=lambda item: item[0]))

    #print out
    for key, value in freq.items(): 
    	if key != list(freq.keys())[-1]:
    		print (end="\'%s\': %d, "%(key, value))
    	else:
    		print ("\'%s\': %d}"%(key, value))
    return freq

#get the key to a list
def get_key(val,my_dict): 
    li = []
    for key, value in my_dict.items(): 
        if val == value:
            li.append(key)
    return li
    		
def start(input):
    #0
    print ('The string being analyzed is: \"' + input + '\"')

    #1
    print (end='1. Sorted dictionary of letter counts: ')
    my_dict = CountFrequency(input)

    #2
    a = max(my_dict.values())
    b = get_key(a,my_dict)
    if len(b) > 1:
        print ('2. Most frequent letter {} appears {} times.'.format(b,a))
    else:
        print ('2. Most frequent letter "{}" appears {} times.'.format(', '.join(b),a))

    #3
    print ('3. Histogram:')
    for key, value in my_dict.items():
        for x in range (int(value)):
            print(key,end='')
        print ()

#start the program here
print('Example Output #1')
start('WAS IT A RAT I SAW')
print('\nExample Output #2')
start('WWAS IT A RAT I SAWW')

