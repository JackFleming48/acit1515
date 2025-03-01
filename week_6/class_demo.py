import sys

'''
Loops - repeat one or more statements X number of timed

X can be a fixed number
X can be the length of a sequence



'''

# def choose_num(num):
#     if num == 1:
#         print()
#         choose_num()
#     elif num == 2:
#         print()
#         choose_num()
#     elif num == 3:
#         sys.exit()

#range(start, stop, step) - returns a range object
nums = (1, 10, 1)
print(nums)

nums = list(range(1, 10, 1))
print(nums)

for i in range(1, 10, 1):
    print(i)

#start can be any number
#stop can be any number
#step can be any number
#start, stop, step can be any number including negative numbers

for i in range(100, -10, -10):
    print(i)
'''
start is 0 (defualt), stop is 10, step is 1 (default) range(10)

start is 1, stop is 10, step is 1 (default)
range (1, 10)

start is 1, stop is 10, step is 2
range(1, 10, 2) --> 1 3 5 7 9
'''

# find ./ -name '*.py' | grep 'lesson'
#finds files with the .py extension in the current directory that contains the name 'lesson'

courses = [1515, 1620, 1630, 1310, 1420, 1100, 1116]

for i in range(len(courses)):
    print(courses[i])
