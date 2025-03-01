from getpass import getpass # DO NOT REMOVE

"""
1. Write a function named 'f' that outputs (i.e. prints()) a hardcoded string including your name and student id. 
"""

def f(name, id):
    print(name, id)

f('Jack Fleming', 'A01331185')

"""
2. Write a function named 'g' that returns a string including your name and student id. On a separate line, call the function and print the result
"""
def g(name, id):
    result = (f"{name}\n{id}")
    return result

n = 'Jack Fleming'
i = 'A01331185'

print(g(n, i))

"""
3. Write a function named 'echo' that accepts a single argument and outputs the argument three times. Call the function to test its output.
"""

def echo(text):
    for x in range(3):
        print(text)

echo("hello")

"""
4. Write three functions:
    - 'add' that accepts two arguments and returns the sum of the two arguments
    - 'subtract' that accepts two arguments and returns the difference of the two arguments
    - 'multiply' that accepts two arguments and returns the product of the two arguments
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

print(add(1, 2), subtract(1, 2), multiply(1, 2))
"""
5. Write a function named 'operation' that accepts three arguments: two numbers and a function. The function argument must be one of the following: 
add, subtract, or multiply (no quotes and no parentheses after the function name!). 'operation' must call the function that is passed in and print 
the result (without any conditional statements or data structures not discussed in class) and must not output any additional text. 
Call the function with different inputs to test all three operations.
"""

def operation(a, b, func):
    res = func(a, b)
    print(res)

operation(1, 2, add)

"""
6. Write a function named 'x' that accepts three arguments and prints them. Use default values to ensure that the function can be called with one, two, or three arguments.
"""

def x(a=5, b=10, c=20):
    print(a, b, c)

x()
x(100)
x(100, 200)
x(100, 200, 300)

"""
7. Write a function named 'y' that accepts a variable number of arguments (i.e. *args) and prints the arguments. Call the function with different numbers of arguments to test the function.
"""

def y(*args):
    print(args)

y(1, 2, 3, 4, 5, 6)
y(1, 2, 3)
y(1)
y()

"""
8. Write a function named 'bedmas' with three parameters. Inside the function, output the result of multiplying the first two arguments and adding the third argument. Call the function and ensure that the order of the keyword arguments passed into the function does not affect the result
"""

def bedmas(a, b, c):
    calc = a*b+c
    print(calc)

bedmas(a= 10, b = 20, c = 30)
bedmas(b = 20, c = 30, a = 10)

"""
9. Write a function called get_username that accepts a single string argument. Inside the function, use input() to ask the user for a username and return the value. The message displayed to the user must be the string argument passed into the function.
"""

def get_username(name):
    user = input(name)
    return user

# get_username("Enter a username: ")

"""
10. Write a function called login that calls the built-in getpass() function and the get_username function. 
The login function must accept a single string argument that is passed to get_username (and then displayed to the user). 
The login function must return a single string: the password concatenated to the username. 
Call the function and print the result.
"""

def login(a):
    return (f"{get_username(a)}{getpass("Enter a password: ")}")

print(login("Enter a username: "))