# single-line comment

"""
multi-line comment

Comments can be used to:
1. document your code (if necessary)
2. disable one or more lines of code

Use ctrl-/ (cmd-/ for mac) to comment/uncomment either the current line or any selected lines
"""
# print('Hello')  # disabled, ignored by the interpreter

"""
Command-line (shell) input and output

output - print()
input - input() allows user to enter some text
"""
# print(input('Please enter your name: '))

# in order to use the value, we need to store it in a variable
"""
A variable is the combination of a stored value and a name (label)
"""
# name = input('Please enter your name: ') # we are creating a variable named 'name', = is the assignment operator

# print(name) # when you want to print the value of the variable, no quotes!

# NOTE: as a rule of thumb, only create variables when you need a value multiple times

name = 'Akila'  # updating the variable
name = 30       # python is 'weakly-typed' - means the data type stored in the variable can change over time

"""
Data Types
int         integer (whole) numbers  e.g. 10, 20, -10
float       decimal numbers e.g. 10.5, -1.25
string      any characters inside of single or double quotes
bool        boolean - only two values: True, False
None        (null) means empty, doesn't exist
"""
x = 20      # int
x = '20'    # string!
is_thursday = True

"""
Conversion Functions
int()
float()
str()
bool()
"""
x = int(x)  # take the current value of x, convert it to an int, and store it back in the same variable (i.e. location)

"""
type() - tells you the current data type of a variable
"""
print(x, type(x))  # LPT: if something in a script is not working, start debugging by printing the value and type of variable(s)

# drivers license
age = input('Please enter your age (17 - 100): ') # input() always returns a string
# print(age, type(age))
years = int(age) - 16 # cannot subtract a string from an int
# print(years, type(years))
# You have been driving for x years
print('You have been driving for ' + str(years) + ' years')

"""
Reminder: Syntax Error - invalid python code
Runtime Error - valid python code, invalid/illegal operation
"""

"""
Operators - symbol that has a special meaning in the language

=       assignment operator

Comparison operators:
==      equality operator
!=      inequality operator
>       greater than
>=      greater than or equal to
<       less than
<=      less than or equal to

Mathematical operators:
+       addition and concatenation (joining things together)
-       subtraction
*       multiplication
/       division
**      exponentation
%       mod (remainder)  
        even % 2 --> 0
        odd % 2 --> 1

hackmd.io/@charris17/acit1515-lesson2
"""

course = '1515'
school = 'BCIT'
instructor = 'Chris'
day = 'Thursday'

# On Thursday we study 1515 with Chris at BCIT
print('On ' + day + ' we study ' + course + ' with ' + instructor + ' at ' + school)

# instead of using string concatenation when you are joining strings with variable values, we can use an 'f' string
print(f'On {day} we study {course} with {instructor} at {school}')