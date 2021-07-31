"""
Zhaowei Gu
Class: CS 521 - Fall 2
Date: Dec 8 2020
Homework Problem #5
Description of Problem (just a 1-2 line summary!):

The formula for calculating the amount of money in a savings account that begins with 
an initial principal value (P) and earns annual interest (i) for (n) years is: P(1 + i)n
Note that i is a decimal, not a percent interest rate: .1 NOT 10%

    Write a python program that does the following:

•   Prompt the user on three lines for principal, percent interest rate and number of years 
    to invest (using descriptive prompts)
    o   Use a while loop to keep prompting until entries are valid
•   Call your function calc_compound_interest() that:
    o   takes the arguments principle, int_rate, years
    o   uses the above formula to calculate the ending value of the account
    o   returns the value
•   Call a second function calc_compound_interest_recursive() that:
    o   takes the arguments principle, int_rate, years
    o   calculates the value recursively – calling a base calculation over and over instead 
        of using the number of year as an exponent.
    o   return that value
•   Print both values with clear descriptions and formatted with thousand commas and 2 decimal 
    places. Then print whether the two values are equal when rounded to 4 decimal places.

"""
#check float
def value_error(user_in):
    try:
        a = float(user_in)
    except:
        #ValueError
        return False
    else:
        if float(user_in) > 0:
            #print (float(user_in))
            return True
        else:
            return False

#check int
def year_error(user_in):
    try:
        a = int(user_in)
    except:
        #ValueError
        return False
    else:
        if int(user_in) > 0:
            #print (float(user_in))
            return True
        else:
            return False

#simple calculation
def calc_compound_interest(principle, int_rate, years):
    return(float(principle) * ((1 + (float(int_rate) * 0.01))**float(years)))


#simple calculation 2
def calc_compound_interest_recursive(principle, int_rate, years):
    result = 0
    for n in range(int(years)):
        if result == 0:
            result = 1 + float(int_rate) * 0.01
        else:
            result = (1 + float(int_rate) * 0.01) * result
    return (result * float(principle))

#check for principal input
x = False
while x == False:
    principal = input('Please enter your initial principal value (2456.75): ')
    x = value_error(principal)
    #print (x)
    if not x:
        print ('Error, please enter your principal value in numbers that is greater than 0')
    else:
        print ('Thank you')

#check for percent_interest_rate input
x = False
while x == False:
    percent_interest_rate = input('Please enter annual interest rate (10%): ')
    percent_interest_rate = percent_interest_rate.strip('%')
    x = value_error(percent_interest_rate)
    #print (x)
    if not x:
        print ('Error, please enter your percent interest rate as (##.#%) that is greater than 0')
    else:
        print ('Thank you')

#check for number_years_invest input
x = False
while x == False:
    number_years_invest = input('Please enter number of years to invest (4): ')
    x = year_error(number_years_invest)
    #print (x)
    if not x:
        print ('Error, please enter years to invest in int that is greater than 0')
    else:
        print ('Thank you')

#calculation done
result_one = calc_compound_interest(principal, percent_interest_rate, number_years_invest)
result_two = calc_compound_interest_recursive(principal, percent_interest_rate, number_years_invest)

#print two result in with discription
print (end='calc compound interest of {}(1 + {}%)**{} give us a result of: '.format(principal, percent_interest_rate, number_years_invest))
print ('{:,.2f}'.format(result_one))
print (end='calc compound interest recursive of {}(1 + {}%)**{} give us a result of: '.format(principal, percent_interest_rate, number_years_invest))
print ('{:,.2f}'.format(result_two))

#set to 4 decimal places
one = ('{:,.4f}'.format(result_one))
two = ('{:,.4f}'.format(result_two))

#check to see if they are the same or not
if one == two:
    print ('when two values [{} == {}] rounded to 4 decimal places they are equal'.format(one, two))
else:
    print ('when two values [{} != {}] rounded to 4 decimal places they are not equal'.format(one, two))
