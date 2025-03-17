def get_name():
    # prompts user for name, returns None if blank, name otherwise
    name = input('Please enter your name: ')

    if name == "":
        return None 

    return name

def get_email():
    # prompts user for email address, returns None if blank, course name otherwise
    email = input("Please enter your email: ")

    if email == "":
        return None
    
    return email
        
def get_course():
    # prompts user for course name, returns None if blank, course name otherwise
    course = input("Please enter your course: ")

    if course == "":
        return None
    
    return course

def get_grade():
    # prompts user for course grade, returns grade if numeric and between 0 and 100, None otherwise
    grade = input("Please enter your grade: ")

    if grade.isdigit():
        grade = int(grade)
        if 100 >= grade >= 0:
            return grade
    
    return None