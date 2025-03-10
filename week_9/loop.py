import json

with open('students.json', 'r') as f:
    data = json.load(f)
    
    for x in data['students']:
        if 'courses' in x:
            for y in x['courses']:
                print(y['course'])