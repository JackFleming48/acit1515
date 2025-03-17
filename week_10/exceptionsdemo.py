import json

'''
Exceptions - handling errors and preventing crashes

Requests - Sending/Receiving data acrpss a network

'''

year = input("Please enter a year: ")



'''
try:
    # code
except:

    #this will catch every possible error


'''

print("script continues")

# catch specific errors

# Syntax errors - when the code is invalid
# Runtime errors - valid code, invalid operation
# Logic error - valid code, valid operation, doesn't do as intended

try:
    with open('student.json', 'r') as f:
        # possible errors
        # 1. file doesn't exit --> FileNotFoundError
        # 2. invalid json --> JSONDecodeError
        data = json.load(f)
        print(data)
except FileNotFoundError as e:
    print(e) # this is the error message given by the interpreter
    print("File does not exist!")
except json.JSONDecodeError:
    print("the file contains invalid data!")

'''
Can use:

try:
    # code that may crash script
except:
    # runs if an error occurs
else:
    # runs if no error occurs

Not the most useful or best practice. Not very logical.


'''
