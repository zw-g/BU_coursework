"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Nov 15 2020
Homework Problem #5
Description of Problem (just a 1-2 line summary!):
0. calculate the BMI
1. ask to see if user wants to use Metric or Imperial
2. ask for user weight & height
3. calcutiona or covertion then calculation
*****(weight(kg)/(height(m)*height(m)))*****
4. print the result for BMI
"""

# Python code to convert string to list 
def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def metricSystem():
	#user enters the weight & height
	user = input("Please enter your weight(Kg) and height(Cm) with space in between\ne.g. if you are 76(kg) & 179(cm) enter \"76 179\": ")

	# Driver code 
	userInformation = Convert(user)
	weight = float(list(userInformation)[0])
	height = float(list(userInformation)[1])

	#calculation and convertion
	height /= 100
	result = (weight/(height*height))
	result = str(round(result, 2))

	#print the result
	print ("\nBMI Categories:\nUnderweight = <18.5\nNormal weight = 18.5–24.9\nOverweight = 25–29.9\nObesity = BMI of 30 or greater\n")
	print ("BMI is being printed: " + result)

def imperialSystem():
	#user enters the weight & height
	user = input("Please enter your weight(lb) height(ft) inches(in) with space in between\ne.g. if you are 167(lb) 5(ft) 11(in) enter \"167 5 11\": ")

	# Driver code 
	userInformation = Convert(user)
	weight = float(list(userInformation)[0])
	feet = float(list(userInformation)[1])
	inches = float(list(userInformation)[2])

	#calculation and convertion
	weight = weight*0.45359
	height = ((feet * 30.48) + (inches * 2.54))/100
	result = weight/(height*height)
	result = str(round(result, 2))

	#print the result
	print ("\nBMI Categories:\nUnderweight = <18.5\nNormal weight = 18.5–24.9\nOverweight = 25–29.9\nObesity = BMI of 30 or greater\n")
	print ("BMI is being printed: " + result)


#INTRO
user = input("do you want to enter Metric(m) or Imperial(i): ")

#MAIN FUNCTION
if user in ['Metric', 'M', 'm', 'metric', 'METRIC']:
	metricSystem()
elif user in ['Imperial', 'I', 'i', 'imperial', 'IMPERIAL']:
	imperialSystem()
else:
	#if the user enters an unexpected input
	print ("please try again sorry I do not recognize " + user)
