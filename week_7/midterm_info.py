'''
Exam is on Monday @ 1:30
3 hours
Closed Book
On Paper
4 versions of the exam, different versions
Covers lesson 1-6

RULES: 
- No talking during the exam
- Nothing on the desk during the exam
- Bring student ID or some form of ID
- If you want to go to the washroom, but you have to give teacher your phone
- Only one person out of the room can go to the washroom at a time
- No music (earbuds, etc)
- If you are more than an hour late, you do no write the exam!!!
- No cheatsheets

2 sections: 
- Short coding answers (28 total, 2 marks each, total of 56)
    - These questions don't include functions
    - Nothing we haven't covered in class
    - Some of these are debugging questions
        - Given wrong code, circle what is wrong with the code

- Multiple choice and T or F questions (22 total, 2 marks each, total of 44) including at least 1 bonus question

Lambdas?    NO
Slice Notation? YES


Which of the following is not a python data type?
a) int
b) float
c) null --> None
d) string
 
Which of the following is not a sequence? #on every version of the exam
a) list
b) set  --> NOT A SEQUENCE, it is unordered
c) tuple
d) string

List of Reminders:

Strings must have quotes around them!

schools = [BCIT, SFU, UBC]  --> NO

This is not a list of strings but variables.

schools = ['BCIT', 'SFU', 'UBC']    --> YES

READ THE QUESTION

Q: Create a variable called course and store the string 151 in it

course = "151"

Q: convert the value in course to an int and store it back into the course variable

course = int(course)    --> YES
course = int('151')   --> NO

school = 'BCIT'
if 'CIT' in 'BCIT': --> NO
if 'CIT' in school: --> YES

list = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
set = {1, 2, 3, 4}

'''

name = "Akila Ramani"

print(name[6::])
print(name[-6::])

'''
slice notation and range:
- start is included
- stop is excluded

range(1, 10) 1 - 9
'ed sweeney' [1:6] --> 'ed swe'


'''