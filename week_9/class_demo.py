import json

'''

Data types:

Basic:
int
float
None
boolean

Sequences:
string
list
tuple

Set

Dictionary - 'mapping' type 
'''

#dog = ['Bella', 12, 'Golden Lab', 14] don't know which value is weight or age
dog = {
    "name": "Bella",
    "age": 12,
    "breed": "Golden Lab",
    "kgweight": 14
}
#like lists, we use square bracket notation to read or update dictionaries, 
#but we use string keys to access values instead of numeric positions
print(dog["age"] )

courses = [
    {"name": "ACIT1515", "grade": 90},
    {"name": "ACIT1620", "grade": 99}
]
courses[1]["grade"]

terms = [
    {
        "term": 1,
        "courses": [
            {"name": "ACIT1515", "grade": 90}
        ]
    },
]
terms[0]["courses"][0]["grade"]

#search for keys in a dictionary
if "name" in dog:
    print('Dog has a name')

for thing in dog:
    print(thing)

for k in dog.keys():
    print(f"Key: {k}")  #keys

for v in dog.items():
    print(f"Item: {v}")


def get_keyitem():
    for k, v in dog.items():
        print(f"Key: {k} Item: {v}")

'''
JSON - JavaScript Object Notation
plain text format for storing or sending/receiving data across a network

API - Application Programming Interface
a set of (related) URLs that send or receive (JSON) data

APIs - weather, stock, sports

Python Dictionary
{
    "name": "Bella",
    "age": "12"
}

JSON Dictionary
{
    "name": "Bella",
    "age": "12"
}

'''

# opening and reading/writing JSON files
# open takes 2 args (string_filename, mode)
#mode can be one of:
# 'w' - write  (this overwrites)
# 'r' - read
# 'a' - append (don't overwrite)

with open('class_demo.json', 'w') as f:
    json.dump()