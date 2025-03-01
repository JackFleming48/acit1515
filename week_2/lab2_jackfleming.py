# Write a program that does the following:

"""
1.  Creates a variable that stores the current year
2.  Prompts the user to enter their name
3.  Prompts the user to enter their birth year
4.  Calculates the age of the user using the current year and birth year
5.  Prints a message to the user (in one line) saying "Hello <name>, you are <age> years old today." 
    where <name> and <age> are the values from steps 2 and 4
6.  Prints 'Goodbye!' on a separate line
"""

year = 2025

name = input("Enter your name: ")
birth = int(input("Enter your birth year (Ex. 2002): "))
age = year - birth

print(f"Hello {name}, you are {age} years old today.\nGoodbye! ")