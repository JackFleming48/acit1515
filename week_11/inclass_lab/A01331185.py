import json
import re

countries = [
    {"country": "America", "continent": "North America"},
    {"country": "Australia", "continent": "Oceania"},
    {"country": "Canada", "continent": "North America"},
    {"country": "Egypt", "continent": "Africa"}
]

continent_set = set()

count = 0
for x in countries:
    continent_set.add(x["continent"])
    
    # print(x["continent"])
    # if x["continent"] != "":
    #     count += 1
    
print(len(continent_set))


# demo = {
#     "ids": {
#         "classes":{
#             "languages":[
#                 "java",
#                 "python",
#                 "html"
#             ]
#         }
#     },
#     "names": [
#         "jack",
#         "dave",
#         "steve"
#     ]
# }

# print(demo["ids"]["classes"]["languages"][0])

'''
Task 1:

sorted() - sort a sequence/set in alphabetical order, returns a sorted copy
strip() - removes whitespace
lower(), upper(), title()

print out all of the instructors one per line in alphabetical order.

'''

with open("lab9-inclass.json", "r") as f:
    data = json.load(f)
    

name_set = set()
editable = []
for x in data:
    if x["name"] != "":
        editable.append(x["name"])
        
for y in range(len(editable)):
    editable[y] = editable[y].strip().lower()
    name_set.add(editable[y])

print(sorted(name_set))

'''
Task 2:

Print out all of the insructors, one per line, in alphabetical order, in the following format:

akila 1
chris 2
johnny 2
tim 1

Where the numbers are the number of course that the instructor teaches
'''
with open("lab9-inclass.json", "r") as f:
    data = json.load(f)
    

# name_set = set()
# course_teacher = [

# ]

# for x in data:
#     x["name"] = x["name"].strip().lower()
#     if x["name"] != "":
#         name_set.add(x["name"])

# print(name_set)

# for y in name_set:
#     course_teacher.append({y: 0})

# for z in course_teacher:
#     for a in data:
#         if a["name"] == z:
#             print(a["course"])
 

# print(course_teacher)

instructors = {}

for d in data:
    n = d["name"].strip().lower()
    if n != "" and n not in instructors:
        instructors[n] = {d["course"]}
    elif n in instructors:
        instructors[n].add(d["course"])

for k, v in instructors.items():
    print(k, len(v))

'''
Task 3

Same as above, in the following format:

chris **
akila *
johnny **
tim *

'''
 
instructors = {}

for d in data:
    n = d["name"].strip().lower()
    if n != "" and n not in instructors:
        instructors[n] = {d["course"]}
    elif n in instructors:
        instructors[n].add(d["course"])

for k, v in instructors.items():
    v = "*" * len(v)
    print(k, v)

'''
Take home:

read a non-json file (e.g. Text)

'''



with open('data.txt', 'r') as f:
    line = f.readline()
    for line in open('data.txt', 'r'):
        print(line)

with open('data.txt', 'r') as f:
    while True:
        line = f.readline()
        if line != "":
            #re is the regular expression module
            #re.sub() allows you to find a pattern in a string and replace it with a new value
            #re.sub(patternToFind, replacement, string)
            # print(line.strip())
            print(re.sub('\n', '', line))
        else:
            break