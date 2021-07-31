"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 22 2020
Homework Problem #6
Description of Problem (just a 1-2 line summary!):

Create a text file containing student records by line and each record is of the format:
•	Name of Student
•	Student ID
•	GPA
For example (you can use your own examples):
	Tyrion Lannister, 1, 3.7
	Daenerys Targaryen, 52, 2.8
	Jon Snow, 13, 3.9
	Sansa Stark, 24, 3.4

Write a program to read the file line by line and store all the records in lists or tuples. 
Hint: you need to create a list of lists or list of tuples.
Afterwards, print the array that you created.

Include the file best practices described in exercise #5.


"""
#load the txt file
openFile = open("studentRecords.txt", "r")

#loop and strip and slit into the list
list_of_lists = [(line.strip()).split(',') for line in openFile]

#close the txt
openFile.close()

#print out the list of lists
for i in list_of_lists:
    for j in i:
        print(j, end=" ")
    print()
