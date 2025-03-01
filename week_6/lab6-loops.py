"""
Write a python program with the following menu options: add a course, update a course, and find a course. 

A course is a list with two values: a name, and a numeric grade. All courses are stored (nested) in a single master list.

Requirements:
    a) The script must not (at any point) crash

    b) Users must be notified when invalid input is given (with indication of what valid input is)

    c) 'update a course' implies that both (or either) the course name and grade can be changed. The course name and/or grade must be modified *in place*, meaning you cannot simply delete and re-add a course with modified values

    d) 'find a course' implies searching by course name

Technical restrictions: 
    a) If no courses have been added, and any menu option other than 'add a course' is chosen, a message must be displayed to the user indicating this 

    b) Users are allowed to keep choosing menu options (i.e. the program should not stop at any point)

    c) No user-defined functions are allowed
"""

courses = []

while True:

    selection = input(f"\nChoose and option \n 1. Add a course \n 2. Update a course \n 3. Find a course \n Your selection: ")

    if selection.isdigit() and int(selection) < 4 and int(selection) > 0:

        if int(selection) == 1:
            c_name = input("\nEnter a course number to add: ")
            c_grade = input("Enter a grade to add to the entered course: ")

            duplicate = False

            for x in range(len(courses)): # range of total course
                if c_name == courses[x][0]: # if inputed course = course found in x
                    duplicate = True
                    print("\nThat course name already exists! Perhaps choose option 2 to edit it instead.")
                    break # if the course is found it breaks the for loop, this is to prevent errors with print and error cases.
            
            if not duplicate:
                if c_grade.isdigit() and 0 <= int(c_grade) <= 100:  # if chosen grade is between 0-100
                    courses.append([c_name, c_grade])   # append the input course name and grade
                    print(courses)
                else:
                    print("please add a valid grade between 0 and 100.")
        
        elif int(selection) == 2:
            count = 1                      
            for x in range(len(courses)):  # print out number of total courses found in courses
                print(f'{count}. {courses[x][0]}') # print the count as a quasi placeholder to represent number. Without this it would start at 0, instead it starts at 1.
                count += 1 # increase the count
            
            if courses:
                course_select = input("Pick a course number to edit: ")
            
                if int(course_select)-1 in range(len(courses)): # if the selected int is within the range of amount of courses
                    print(f"\nCourse name: {courses[int(course_select)-1][0]} \nGrade: {courses[int(course_select)-1][1]}\n") # print correlating course name and grade
                    new_course = input("\nEnter a new course name: ")
                    new_grade = input("Enter a new course grade: ")
                    if new_grade.isdigit() and 0 <= int(new_grade) <= 100: # same clause as previous section.
                        courses[int(course_select)-1][0] = new_course  
                        courses[int(course_select)-1][1] = int(new_grade)
                        print(courses)
                    else:
                        print("\nPlease add a valid grade between 0 and 100")
                else:
                    print("Please pick a number from the given options!\n")
            else:
                print("\nNo courses have been added yet! Please choose 1 to first add a course.")

        elif int(selection) == 3:
            if courses:
                val = [] # this will eventually hold the locations of the matching course and grade.
                find_course = input("Enter a course to find: ")
                for x in range(len(courses)): # range of total course
                    if find_course == courses[x][0]: # if inputed course = course found in x
                        val = [courses[x][0], courses[x][1]]  # location at the found matching course is hardcoded as val, not append in case user wants to check another course it resets each time
                        print(f"\nCourse Name: {val[0]}\nGrade: {val[1]}") # print with formatting
                        break # if the course is found it breaks the for loop, this is to prevent errors with print and error cases.
                if find_course != courses[x][0]:
                        print("\nThat course is not found. Please type the exact course name entered.")
            else:
                print("\nNo courses have been added yet! Please choose 1 to first add a course.")

    else:
        print("\nInvalid Option. Please choose 1, 2, or 3.")