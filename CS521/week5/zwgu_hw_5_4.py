"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Dec 8 2020
Homework Problem #4
Description of Problem (just a 1-2 line summary!):

Prompt for a file name of text words. 
Words can be on many lines with multiple words per line.

Read the file and convert the words to a list. 

Call a function you created called list_to_words(), that takes a list as an argument and returns a list that contains only words that occurred once in the file.

Print the results of the function with an appropriate description.

Think about everything you must do when working with a file.
"""

import string
#check numbers
def value_error(user_in):
    try:
        a = float(user_in)
    except:
        #ValueError
        return True
    else:
        return False

def check_file_name(user_in):
    try:
        openFile = open(user_in, "r")
        openFile.close()
    except:
        print('The file ' + user_in + ' does not exist in the directory')
        return False
    else:
        return True

def list_to_words(user_list):
    result = []

    #for all the elements count is it only show up once then add the to list
    for element in user_list:

        #words do not include #, so if its numbers do not care it
        if (value_error(element)):
            if user_list.count(element) == 1:
                #print('good')
                result.append(element)
    return result

#ask for input
user_in = input('Please enter the .txt file name that you would like to open: ')+'.txt'

#check if file exist
if (check_file_name(user_in)):
    # load the txt file
    openFile = open(user_in, "r")

    # change txt list
    words = openFile.read().strip().lower()
    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.split()

    print ('Printing the words that occurred once in the ' + user_in + ' file: ')

    #print all the words that used once
    print (*list_to_words(words), sep = ", ")

    # close the txt
    openFile.close()
