import json

"""
Data Types

Basic:
int
float
None
bool

Sequences:
string
list
tuple

Set

Dictionary - 'mapping' type
"""
dog = ['Bella', 12, 'Golden Lab', 14]
# dog[1]
# course = ['ACIT1515', 25, 1, 50]
dog = {
    "name": "Bella",
    "age": 12,
    "breed": "Golden Lab",
    "kgweight": 14
}
# like lists, we use square bracket to read/update dictionaries, but we use string keys to access values in stead of numeric positions
print(dog)  # { "name": "Bella", ... }
print(type(dog)) # <class 'dict'>
print(dog["age"])
dog["age"] = 13
# dog = {1, 2, 3, 4, 5} # set

courses = [
    ["ACIT1515", 90],
    ["ACIT1620", 99],
    ["ACIT1630", 45]
]
print(courses[1][1])
courses = [
    { "name": "ACIT1515", "grade": 90 },
    { "name": "ACIT1620", "grade": 99 }
]
courses[1]["grade"]

terms = [
    {
        "term": 1,
        "courses": [
            { "name": "ACIT1515", "grade": 90 }
        ]
    },
]
terms[0]["courses"][0]["grade"]

# Loop through dictionaries
# for thing in dog:
#     print(thing) # keys

# for k in dog.keys():
#     print(k) # keys

# for v in dog.values():
#     print(v) # values

# for k, v in dog.items():  # gives you keys and values
#     print(f'{k}: {v}')

# # Search for keys in a dictionary
# if "name" in dog:
#     print('Dog has a name')


"""
JSON - JavaScript Object Notation
plain text format for storing or sending/receiving data across a network

Python dictionary 
{
    "name": "Bella",
    "age": 12
}
JSON object
{
    "name": "Bella",
    "age": 12
}


API - Application Programming Interface
a set of (related) URLs that send or receive (JSON) data

An 'endpoint'/resource is one of those URLs

APIs - weather, stock, sports
e.g.
https://jsonplaceholder.typicode.com/
https://jsonplaceholder.typicode.com/users

"""

# opening and reading/writing JSON files
# open(string_filename, mode)
# mode can be one of:
# 'w' - write   (overwrites! replaces! removes!)
# 'r' - read
# 'a' - append  (doesn't overwrite)

# WRITE
# with open('data.json', 'w') as f:
    # f *is* the file, and we need to use it to read/write the file

    # json.dump(dict/list, file)

    # NOTE: json is part of the standard python module, but not enabled by default. To use it we have to import json
    # json.dump(dog, f)
    # json.dumps()

# READ
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data, type(data))


# Two ways to run python files:
# as a script (self-contained application)
# as a module (a file that usually contains reusable functions that are imported into a script)