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
3.
After a blank line, the same output, but applied to Archibald Montague Abercrombie
4.
After a blank line, the same output, but applied to Cleopatra Anastasia Montgomery
'''

greeting1 = "Greetings from a beginning Python programmer."
question1 = "Do you want to be addressed as ...\n"
reuse = ".......................................======>"
print(greeting1)
print(question1)

style1 = "{0}{1} {2} {3}?"
style2 = "{0}{1} {2}?"
style3 = "{0}Mr./Ms. {1} {2} {3}?"
style4 = "{0}Dear {1}?\nor"
style5 = "{0}{1},{2} {3}?"

Jane1 = "Jane"
Jane2 = "Margaret"
Jane3 = "Doe"
print(style1.format(reuse,Jane1,Jane2,Jane3))
print(style2.format(reuse,Jane1,Jane3))
print(style3.format(reuse,Jane1,Jane2,Jane3))
print(style4.format(reuse,Jane1))
print(style5.format(reuse,Jane3,Jane1,Jane2))
print("\n")

A1 = "Archibald"
A2 = "Montague"
A3 = "Abercrombie"
print(style1.format(reuse,A1,A2,A3))
print(style2.format(reuse,A1,A3))
print(style3.format(reuse,A1,A2,A3))
print(style4.format(reuse,A1))
print(style5.format(reuse,A3,A1,A2))
print("\n")

A1 = "Cleopatra"
A2 = "Anastasia"
A3 = "Montgomery"
print(style1.format(reuse,A1,A2,A3))
print(style2.format(reuse,A1,A3))
print(style3.format(reuse,A1,A2,A3))
print(style4.format(reuse,A1))
print(style5.format(reuse,A3,A1,A2))
