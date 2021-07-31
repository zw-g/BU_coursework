"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #5
Description of Problem (just a 1-2 line summary!):

Create a test file with a single sentence of 20 words. 

Read the file, insert appropriate new line characters (\n) and write the test 
to a new text file that contains four lines of five words.

Print an error message and stop if the sentence in the file has other than 20 words.

Test the input file for existence and not crash if the file does not exist.

Remember to properly close the files.

"""
#open and load in the txt
openFile = open("testFile.txt", "r")

#read and split
words = openFile.read().split()

#close it
openFile.close()

#check to see if it is over 20
if (len(words) == 20):
	print ("all good")
	with open("newFile.txt", "w") as output:
		n = 1											#if number % 4 = 0 then start a new line
		for listItem in words:
			if (n % 4 != 0):
				output.write('%s ' % listItem)
				n += 1
			else:
				output.write('%s\n' % listItem)
				n += 1

else:
	# error message
	print ("Error! the test file has more or less than 20 words")
