import json 
from pathlib import Path
from colorama import Fore
# ensure you have lab7-dictionaries-json.py and lab7_lib.py in the same folder, then import lab7_lib
import lab7_lib

# uses get_name() and get_email()
# add a student to the database
def add_student():
    name = lab7_lib.get_name()
    if name == None:
        print('Invalid username')
    else:
        email = lab7_lib.get_email()

    with open('students.json', 'r') as read:
        is_mt = json.load(read)
        if not is_mt: # if is_mt contains nothing, initialize in the intended format
            data = {
                'students': []
            }
        else:
            data = is_mt # else, date = the populated json dict
    
    print(f"Added studend: {{'name': {name}, 'email': {email}}}")
    data['students'].append({'name': name, 'email': email}) # append the dict to the list of students

    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

    

# uses get_name() and get_email()
# choose a student from the database, return dict if found or None
def choose_student():
    name = lab7_lib.get_name()
    email = lab7_lib.get_email()

    with open('students.json', 'r') as f:
        data = json.load(f)
        for x in data['students']: # loop through students
            if x['name'] == name and x['email'] == email: # if both email and name are equal to student dict at x
                return x
        
        return None

    
# uses get_course() and get_grade()
# adds a course to a student in the database
def add_course(current_student):

    course = lab7_lib.get_course()
    grade = lab7_lib.get_grade()

    with open('students.json', 'r') as f:
        data = json.load(f)
    
    for x in data['students']: 
        if x['name'] == current_student['name']: # if name at x is equal to name of current student
            if 'courses' not in x: # if 'courses' not in current student dict, initialize an empty list for courses
                x['courses'] = []
            print(f"Added course: {{'course': {course}, 'grade': {grade}}}")
            x['courses'].append({'course': course, 'grade': grade}) # append course and grade to current_students list of courses
    
    with open('students.json', 'w') as wr:
        json.dump(data, wr, indent=4)
                


# uses get_course()
# removes a course from a student in the database
def drop_course(current_student):
    course = lab7_lib.get_course()

    with open('students.json', 'r') as f:
        data = json.load(f)
    
    for x in data['students']: 
        if x['name'] == current_student['name']:
            if 'courses' in x: # if courses list is present
                for y in range(len(x['courses'])): # i learned del needs an index so that is why i used range(len)
                    if x['courses'][y]['course'] == course: # if course and index y equals selected course
                        print(f"Deleted: {x['courses'][y]}")
                        del x['courses'][y] # delete the whole dict in that index
                        break
            else:
                return

    with open('students.json', 'w') as wr:
        json.dump(data, wr, indent=4)



# prints the names of all students in the database
def view_courses(current_student):
    
    with open('students.json', 'r') as f:
        data = json.load(f)

    for x in data['students']: # for x in student dict
        if x['name'] == current_student['name']: # if name at x is equal to current_student name
            if 'courses' in x: # if courses list is present
                print("Here are the courses: ")
                for y in x['courses']: # iterate each course found in course and print
                    print(f"{y['course']}")

def begin_main_loop():
    choice = None
    current_student = None
    main_menu = [
        'Add Student (a)',
        'Edit Student (e)'
    ]
    student_menu = [
        'Add Course (c)',
        'Drop Course (d)',
        'View Courses (v)'
    ]

    while choice != 'q':
        if current_student is None:
            for i, v in enumerate(main_menu):
                print(Fore.GREEN + f'{i+1}. {v}')
        else:
            for i, v in enumerate(student_menu):
                print(Fore.YELLOW + f'{i+1}. {v}')

        choice = input(Fore.RESET + '\nPlease choose a menu option \n(enter "q" to quit or "m" to return to main menu): ')
        
        match choice:
            case 'a':
                if current_student is not None:
                    continue
                add_student()

            case 'e':
                if current_student is not None:
                    continue

                student = choose_student()
                if student is not None:
                    current_student = student

            case 'c':
                if current_student is None:
                    continue
                add_course(current_student)

            case 'd':
                if current_student is None:
                    continue
                drop_course(current_student)

            case 'v':
                if current_student is None:
                    continue
                view_courses(current_student)

            case 'm':
                current_student = None

def seed():
    f = Path('./students.json')
    if not f.exists() or (f.exists() and f.stat().st_size == 0):
        f.write_text('[]')

if __name__ == '__main__':
    seed()
    begin_main_loop()
