# # 1. Change only one operator between lines 2 and 4 such that line 4 prints 'True'
course = '1515'
number = course
print(number == '1515')

# # 2. Change only line 10 such that the sentence (with spaces) "We are learning Python in 1515 at BCIT" is output
school = 'BCIT'
course = 1515
language = 'Python'
print(f"We are learning {language} in {course} at {school}")

# # 3. Change lines 13 and/or 14 such that whatever number is entered by the user is correctly squared and output
fave = input('Please enter your favourite number: ')
print('Your favourite number squared is', int(fave)**2)

# 4. Change only one operator between lines 19 and 21 such that line 23 prints 'True'. Note that only operators can be changed - no changing variables, creating new variables, adding or removing lines etc.
first = 1515
second = 2**0 # = 1
third = second + second # = 2
fourth = first / third # = 1515 / 2 = half of 1515
fifth = fourth + fourth # = half of 1515 + half of 1515
sixth = int(fifth) # int(1515)
print(sixth == first)