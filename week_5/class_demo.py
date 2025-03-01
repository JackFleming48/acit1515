# money_saved = 5000

# if money_saved < 5000:
#     print('you saved some money')
# elif money_saved > 5000 and money_saved < 10000:
#     print('You will be okay')
# elif money_saved > 10000:
#     print('rich')
# else:
#     exit

name = 'Jacka aFleming'

# print(len(name)-1)

# print(name[0::2])

# print(name.upper()) #return string in upper case,
                    # string is not actually changed
                    # just a copy is returned

#concatenating
# program = 'acit'
# course = '1515'

# print(program + course)

#print(name[2:3])

#check if a value appears in a string

# if 'n' in name:
#     print('The name contains the character N')

# if 'cit' in 'bcit':
#     print('cit is in bcit')

print(name.count('a'))

#index() - where a value is in a sequence

# print(name.index("F"))

#if value is not in string error is produced

'''
String - a sequence of characters
List - a sequence of values

'''

schools = []

letters = "abcdefghijklmnopqrstuvwxyz"

for x in letters:
    schools.append(x)

mixed = [1, 10.5, True]

print(mixed[1])

nested = [['a', 'b', 'c'], [1, 2, 3]]

print(nested[0][2])

#every sequence can be followed by square brackets


'''
Tuples - immutable lists

    no.append()
    no grades[1] = 100 "item assignment"

'''

grades = (90, 55, 99, 94)

'''
int()
float()
bool()
str()
list()
tuple()
set()
'''

print(list(name))


'''
Sets - NOT A SEQUENCE, unordered, cannot contain
duplicate values (duplicate values are discarded),
declared using {}

'''

# number_set = {1, 2, 3, 4, 2, 3, 5} 

#second 2 is not counted

# print(len(number_set))

# sets use .add() to add values to sets

# number_set.add(5)

# print(number_set)

#empty_set = {} # This is not an empty set, it is
                # an empty dictionary

# empty_set = set()

#this is an empty set

# with sets we can use .intersection()

instructor1 = 'akila ramani'
instructor2 = 'tom lane'

# what are the letters that these two names
# have in common

instructor1 = set(instructor1.strip())
instructor2 = set(instructor2.strip())
#strip removes whitespace


# print(instructor1, instructor2)


print(instructor1.intersection(instructor2))

#prints the values of the same letters in instructors