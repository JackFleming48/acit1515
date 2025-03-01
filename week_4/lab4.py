
"""
Write a program that does the following:

1.  Creates a variable that stores the current year
2.  Prompts the user to enter their name
3.  Prompts the user to enter their birth year
4.  Calculates the age of the user using the current year and birth year
5.  Prints a message to the user (in one line) saying "Hello <name>, you are <age> years old today." 
    where <name> and <age> are the values from steps 2 and 4
6.  Prints 'Goodbye!' on a separate line

with the addition of conditional statements to ensure that:

a) the user is notified if an invalid value (for birth year) is entered
b) the message from step 5 is only output if a numeric value is entered
c) the program does not crash if the user enters an empty string (by hitting the enter key without typing any text) for name or birth year
"""
def user_age():
    curr_year = 2025
    name = input("What is your name? ")
    birth = input("What year were you born? ")
    
    if validate_birth(birth) and validate_name(name):
        birth = curr_year - int(birth)
        print(f"Hello {name}, you are {birth} years old today. \nGoodbye!")
        return
    elif not validate_birth(birth):
        print("Please do not leave your birth year blank, include special characters, or include letters")
    else:
        print("Please do not leave your name blank.")
    user_age()


def validate_name(name):
    if name == '':
        return False
    else:
        return True

def validate_birth(num):
    if num.isdigit():
        return True
    else:
        return False
    

user_age()