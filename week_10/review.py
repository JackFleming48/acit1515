import json

course = {
    "grades": [

    ],
    "name": "acit1515"
}

for k, v in course.items():
    print(k, v)

for k in course.keys():
    print(k)

for k in course:
    print(k)

with open('data.json', 'w') as f:
    json.dump(course, f, indent=4)