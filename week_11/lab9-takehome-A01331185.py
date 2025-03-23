import re

# '''
# task 1
# '''

# def matrix2(): #not my proudest work :(

#     lst = []
#     names = []

#     for x in open("lab9-takehome.txt", "r"):
#         if x == "":
#             pass
#         else:
#             lst.append(re.sub("\n", "", x))
    
#     for x in lst:
#         if x == "":
#             lst.remove(x)

#     for x in range(len(lst)):
#         if "" in lst[x]:
#             names.append(lst[x].split())

#     lst = names
#     names = {}

#     for x in lst:
#         names.update({x[0]: len(x[1::])})

#     return names

# print(matrix2())

# '''
# task 2
# '''

# def instructor2():

#     tup = []

#     for k, v in matrix2().items():
#         tup.append((k, v))

#     return sorted(tup)

# print(instructor2())

# '''
# task 3
# '''

# def instructors2(): 

#     tup = []

#     for k, v in matrix2().items():
#         tup.append((k, v * "*"))

#     return sorted(tup)

# print(instructors2())

# '''
# task 4
# '''

# def instructors2_format(): 
#     tup = instructors2()
#     tup = list(tup)

#     for x in tup:
#         print(x[0], x[1])

    

# instructors2_format()


# '''
# task 5
# '''

# def leet(strang): # :(
#     for x in strang:
#         strang = re.sub("e", "3", strang)
#         strang = re.sub("E", "3", strang)
#         strang = re.sub("l", "1", strang)
#         strang = re.sub("L", "1", strang)
#         strang = re.sub("t", "7", strang)
#         strang = re.sub("T", "7", strang)
#         strang = re.sub("s", "5", strang)
#         strang = re.sub("S", "5", strang)
#         strang = re.sub("a", "4", strang)
#         strang = re.sub("A", "4", strang)


#     return strang

# print(leet("Leetspeak leetSpeaK"))

# '''
# task 6
# '''

# def seperate_and_sort(strang): #im so sorry lol
#     nums = []
#     strs = []
#     strang = "".join(strang.lower().strip().split())
#     for x in strang:
#         if x.isdigit():
#             nums.append(x)
#         else:
#             strs.append(x)

#     strang = ""
#     for x in sorted(strs):
#         strang = strang + x
#     for x in sorted(nums):
#         strang = strang + x

#     return strang

# print(seperate_and_sort("Chris Harris ACIT1515"))

# '''
# task 7
# '''

# def list2dict(lst):
#     newlst = {}
#     if len(lst) % 2 == 1:
#         return ""
#     else:
#         for x in range(len(lst)):
#             if type(lst[x]) == int or type(lst[x]) == str: 
#                 if x % 2 == 0:
#                     if lst[x] not in newlst:
#                         newlst.update({lst[x]: lst[x+1]})
#                     else:
#                         continue
#             else:
#                 pass

#     return newlst


            
        

# print(list2dict(['Chris', 'ACIT1515', 'Akila']))
# print(list2dict(['Chris', 'ACIT1515', ['Akila'], 'ACIT1620', 'Tim', 'ACIT2515']))
# print(list2dict(['Chris', 'ACIT1515', 'Chris', 'ACIT2811']))
# print(list2dict(['Chris', 'ACIT1515', 'Akila', 'ACIT1620', 'Chris', 'ACIT2811']))

# '''
# task 8
# '''

# def count_by_key(data, val):
#     lst = []
#     for x in range(len(data)):
#         for k, v in data[x].items():
#             if k == val and v not in lst:
#                 lst.append(v)
#     return len(lst)
                
# print(count_by_key([{'a': 2}], 'a'))
# print(count_by_key([{'a': 2, 'b': 4}, {'a': 1}, {'a': 1, 'b': 4}, {'a': 4, 'b': 4}], 'a'))
# print(count_by_key([{'a': 2, 'b': 4}, {'a': 1}, {'a': 1, 'b': 4}, {'a': 4, 'b': 4}], 'b'))

'''
task 9
'''

def compat(a, b):
    try:
        if type(a) != type(b):
            a = type(b)(a)
            return a+b
    except TypeError:
        return ""

    return a+b

print(compat(2, 2))
print(compat('2', '2'))
print(compat('2', 2))
print(compat('15', ['1', '5']))
print(compat(None, 10))
print(compat(None, 'such'))

'''
task 10
'''

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def operation(lhs, rhs, f, count):
    if count == 1:
        return f(lhs, rhs)
    else:
        while count > 0:
            num = f(lhs, rhs)
            rhs = num
            lhs = num
            count -= 1
    return num


print(operation(4, 3, add, 2)) # 4+3=7, 7+7=14
print(operation(4, 4, subtract, 3)) # 4-4=0, 0-0=0, 0-0=0
print(operation(1, 2, multiply, 5)) # 1*2=2, 2*2=4, 4*4=16, 16*16=256, 256*256=65536
print(operation(4, 4, divide, 2))