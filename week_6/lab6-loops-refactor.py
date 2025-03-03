courses = []

def choice():
    selection = input(f"\nChoose and option \n 1. Add a course \n 2. Update a course \n 3. Find a course \n Your selection: ")
    
    if check_choice(selection):

        if int(selection) == 1:
            choice_one()
        
        elif int(selection) == 2:
            choice_two()
        
        elif int(selection) == 3:
            choice_three()

    elif not check_choice(selection):
        print("\nInvalid Option. Please choose 1, 2, or 3.")
        choice()


def choice_one():
    c_name = input("\nEnter a course number to add: ")
    c_grade = input("Enter a grade to add to the entered course: ")

    if is_duplicate(c_name):
        print("\nThat course name already exists! Perhaps choose option 2 to edit it instead.")
        choice()

    elif not is_duplicate(c_name):
        if is_valid_grade(c_grade):
            courses.append([c_name, c_grade])   # append the input course name and grade
            print(courses)
            choice()

        elif not is_valid_grade(c_grade):
            print("please add a valid grade between 0 and 100.")
            choice()

def choice_two():
    count = 1                      
    for x in range(len(courses)):  # print out number of total courses found in courses
        print(f'{count}. {courses[x][0]}') # print the count as a quasi placeholder to represent number. Without this it would start at 0, instead it starts at 1.
        count += 1 # increase the count

    if is_courses(courses):
        course_select = input("Pick a course number to edit: ")


        if course_select.isdigit():
            if is_within_range(course_select):
                print(f"\nCourse name: {courses[int(course_select)-1][0]} \nGrade: {courses[int(course_select)-1][1]}\n") # print correlating course name and grade
                new_course = input("\nEnter a new course name: ")
                new_grade = input("Enter a new course grade: ")

                if is_valid_grade(new_grade):
                    courses[int(course_select)-1][0] = new_course  
                    courses[int(course_select)-1][1] = int(new_grade)
                    print(courses)
                    choice()

                elif not is_valid_grade(new_grade):
                    print("\nPlease add a valid grade between 0 and 100")
                    choice()

            elif not is_within_range(course_select):
                print("\nPlease pick a number from the given options!")
                choice()
        
        elif not course_select.isdigit():
            print("\nPlease pick a number from the given options!")
            choice()

    elif not is_courses(courses):
        print("\nNo courses have been added yet! Please choose 1 to first add a course.")
        choice()  

def choice_three():

    if is_courses(courses):
        val = [] # this will eventually hold the locations of the matching course and grade.
        find_course = input("Enter a course to find: ")
        course_details = get_course(find_course)

        if course_details:
            val = course_details  # location at the found matching course is hardcoded as val, not append in case user wants to check another course it resets each time
            print(f"\nCourse Name: {val[0]}\nGrade: {val[1]}") # print with formatting
            choice()


        elif not course_details:
            print("\nThat course is not found. Please type the exact course name entered.")
            choice()
            
    elif not is_courses(courses):
        print("\nNo courses have been added yet! Please choose 1 to first add a course.")
        choice()

def get_course(find_course):
    for x in range(len(courses)):
        if courses[x][0] == find_course:
            return [courses[x][0], courses[x][1]]
    
    return None

def is_within_range(course_select):

    if int(course_select)-1 in range(len(courses)): # if the selected int is within the range of amount of courses
        return True
    
    else:
        return False
    
def is_courses(courses_list):

    if courses_list:
        return True
    
    else:
        return False

def is_valid_grade(c_grade):

    if c_grade.isdigit() and 0 <= int(c_grade) <= 100:  # if chosen grade is between 0-100
         return True
    
    else:
         return False

def is_duplicate(c_name):

    for x in range(len(courses)): # range of total course
        if c_name == courses[x][0]: # if inputed course = course found in x
            return True
    
def check_choice(selection):   

    if selection.isdigit() and int(selection) < 4 and int(selection) > 0:
        return True
    
    else:
        return False
    
choice()