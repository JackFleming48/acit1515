# def sum(num1, num2):
#     calc = num1 + num2
#     return calc

# int1 = int(input("Enter a num:"))
# int2 = int(input("Enter another num: "))

# print(sum(int1, int2))

# def f(p1=1, p2=2, p3=3):
#     print(p1,p2,p3)

# f(10, 20, 30)
# f(10, 20)

# f(a, b, c = 1) OK
# f(a, b=1, c=1) OK
# f(a=1, b, c) NOT OK

# default values in functions must be at the end.

#We can also use variable arguments (a variable name with a star before it, 
# at the end of the parameter list) to pass different numbers of values into a function.

# def f(a, b, *args):
#     print(a, b, args) # note how the star only appears in the param list

# f(10, 20, 30, 40, 50)

#The return keyword

#We can 'call' a function and the function can 'return' (respond) with a value
# def sum(lhs, rhs):
#     #return - return without a arguments with stop the function and anything underneath will become unreachable
#     #return also always ends a function.
#     return lhs + rhs #returns this value

# result = sum(10, 20)

# print(result)

# print(print()) #prints "none"

# Python has anonymous functions called lambdas
lambda x: x * 2
