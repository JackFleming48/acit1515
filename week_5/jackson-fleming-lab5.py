import sys

"""
In Lab 5b you are writing a strong password checker.

The user must be asked to input a password, and you must perform the following checks to determine whether the password they chose was strong or weak:

1. The password cannot be blank
 
2. The password must be at least 16 characters long

3. The password can only contain letters, no numbers or special characters

3. The password must have uppercase AND lowercase letters (hint: use .islower() and .isupper() on your string variable to test)

4. The password cannot have any repeating characters (consecutive AND non-consecutive)

If all of the above conditions are met, print a message (using their username) to the user indicating that they have successfully chosen a strong password.

Otherwise print a message to the user indicating that the password they chose is not strong.
"""

def check_pass(usern, pword):
    if len(pword) < 16:
        print("password not long enough")
        sys.exit()
    elif " " in pword:
        print("Cannot contain blank spaces")
        sys.exit()
    elif check_up_low(pword) == False:
        print("Password must contain atleast one upper and lower case character.")
    elif not check_dupe(pword):
        print("Your password cannot contain duplicate characters!")
    else:
        print(f"{usern}, Your password is strong!")

    
    

def check_up_low(pword):
    is_lower = False
    is_upper = False

    for char in pword:
        if char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
    if is_upper and is_lower:
            return True
    else:
        return False

def check_dupe(pword):
    set_pass = set(pword)

    if len(set_pass) != len(pword):
        return False
    else:
        return True

user = input("What is your username? ")
p_word = input("What is your password? ")
check_pass(user, p_word)


"""
1. 
a). Create a variable that stores an empty list

b). Use multiple input() statements to get five numbers from the user. Each value the user enters must be converted to int and stored in the variable created in step a. NOTE: you do not need to handle invalid values entered by the user

c). Once all five values have been added to the list (i.e. the numbers variable), calculate the average of the numbers and print a message to the user indicating what this value is, e.g.
    The average of all values you entered is 12
"""
empty_list = []

user_input1 = input("Enter a number that will be put into a list: ") 
user_input2 = input("Enter a number that will be put into a list: ")
user_input3 = input("Enter a number that will be put into a list: ")
user_input4 = input("Enter a number that will be put into a list: ")
user_input5 = input("Enter a number that will be put into a list: ")

empty_list.append(int(user_input1))
empty_list.append(int(user_input2))
empty_list.append(int(user_input3))
empty_list.append(int(user_input4))
empty_list.append(int(user_input5))

avg =  (empty_list[0] + empty_list[1] + empty_list[2] + empty_list[3] + empty_list[4] ) / len(empty_list)

print(f'The average of all the values you entered is {avg}.')

"""
2. 
a). Using the 'provinces' variable below, print all six provinces, one per line with a number in front of them, e.g.:
    
    1. British Columbia
    2. Alberta
    3. Saskatchewan
    4. Manitoba
    5. Ontario
    6. Quebec

    NOTE: Province names must be read from the list, not hard-coded!

b). Using input(), ask the user to choose a province by its number

c). If the user enters an invalid value (number out of range, or non-numeric character), allow the program to end using sys.exit()

d). Use input() to ask the number for a single letter

e). If the user enters a single alphabet character (hint: use .isalpha()), print a message to the user indicating:
    - whether the letter appears in the province name
    - how many times the letter appears in the province name

Below is example output for question 2

    Please choose a province:
    1. British Columbia
    2. Alberta
    3. Saskatchewan
    4. Manitoba
    5. Ontario
    6. Quebec

    >> 3
    You chose Saskatchewan. Please choose a single letter:

    >> a
    The letter 'a' appears in Saskatchewan 3 times
"""
provinces = ['British Columbia', 'Alberta', 'Saskatchewan', 'Manitoba', 'Ontario', 'Quebec']

def disp(ls_provinces):

    count = 1                       # count for 1. 2. 3. etc
    for x in ls_provinces:             # loop through list
        print(f'{count}. {x}')      # print count and province name so 1. British columbia
        count+=1                    # increase count each time to increase with iteration

def choose(prov):

    user_input = input("choose a province by number, enter the provinces corresponding number: ")   # ask for user input


    if user_input.isalpha() or int(user_input) > len(provinces) or int(user_input) == 0:    # if input is string, or greater than length of provinces list
        sys.exit()                                                    # end the program.
    else:
        chosen = prov[int(user_input)-1]                            # else if all is good chosen province entered number minus one
                                                                    # this is to display the correct province in next step
                                                                    # as the first province is 1 not 0 and so on.
        return chosen

def letters(prov_name, letter): # simply returns the count of a letter within a selected province
    
    return prov_name.count(letter)

disp(provinces)   #function to display options
chosen = choose(provinces) # function that handles incorrect input and declares the chosen province

choose_letter = input(f'You chose {chosen}. Please choose a single letter: ') 

get_letters_in_province = (letters(chosen, choose_letter))  # function that gets how many times the user selected letter appears in the chosen province

print(f"The letter {choose_letter} appears in {chosen} {get_letters_in_province} times") # fin
"""
3.
a). Using the final_grades variable below, print all existing grades, nicely formatted one per line, e.g.
    
    Final Grades
    Term 1: 75
    Term 2: 20
    Term 3: 50

b). Using input(), ask the user to enter a mark for Term 4. If the user enters a valid mark (numeric, between 1 and 100), add an entry to the final_grades list

c). If the user enters an invalid grade, add a new entry to the final grades for Term 4 with a mark of zero

d). Calculate the average of all the grades and conditionally print a message to the user indicating what their grade is and whether they passed or failed
"""
final_grades = [
    ['Term 1', 75],
    ['Term 2', 20],
    ['Term 3', 50]
]

def display(lst_grades):                                    # displays the Finals Grades for each term in specified format

    print('Final Grades')                                   # Before loop to not print range(len(lst_grades)) times
    for x in range(len(lst_grades)):                        # range of length of items in final_grades
        print(f'{lst_grades[x][0]}: {lst_grades[x][1]}')    # print items found in list x at location 0 and 1 

def user_input(lst_grades):                                 # accepts input for 4th grade term
    
    user_grade = input("Enter a mark for term 4: ")         

    if not user_grade.isdigit():                            # checks if not digit
        lst_grades.append(["Term 4", 0])                    # if no digit term 4 grade is 0
    elif int(user_grade) <= 100 and int(user_grade) >= 0:   # if digit is within constraints append user grade to list
        lst_grades.append(["Term 4", user_grade])           
    else:                                                   # in any other case grade will be 0
        lst_grades.append(["Term 4", 0])
    return lst_grades
        
def calc_avg(lst_grades):                                   # calculates avg grade
    avg = 0                                                 # initialize avg as -
    for x in lst_grades:                                    # add x[1] to avg
        avg += int(x[1])    
    avg = avg / len(lst_grades)                             # take avg and divide by total number of entries
    
    if avg >= 50:
        print(f'Your grade is {avg}, you passed!')
    else:
        print(f'Your grade is {avg}, you failed!')

display(final_grades)                                       # call function display
final_grades = user_input(final_grades)                     # final_grade now has term 4 value appended
calc_avg(final_grades)                                      # calculate average - fin