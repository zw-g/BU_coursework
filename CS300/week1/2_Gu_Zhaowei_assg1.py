'''
Intent: Begin to provide options for the form of one person to be addressed.

Postconditions: The following are on the console (excluding the numbering):
1.
Greetings from a beginning Python programmer.
2.
Do you want to be addressed as ...
.......................................======>Jane Margaret Doe?
.......................................======>Jane Doe?
.......................................======>Mr./Ms. Jane Margaret Doe?
.......................................======>Dear Jane?
or 
.......................................======>Doe, Jane Margaret?
'''

greeting1 = "Greetings from a beginning Python programmer."
question1 = "Do you want to be addressed as ..."
reuse = ".......................................======>"
print(greeting1)
print(question1)
print(reuse +"Jane Margaret Doe?")
print(reuse +"Jane Doe?")
print(reuse +"Mr./Ms. Jane Margaret Doe?")
print(reuse +"Dear Jane?")
print("or")
print(reuse +"Doe, Jane Margaret?")