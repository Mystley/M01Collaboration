"""
This program is intended to accept student names and GPAs and test if the student
 qualifies for either the Dean's List or the Honor Roll. The app will specifically:
    ○ ask for and accept a student's last name.
    ○ quit processing student records if the last name entered is 'ZZZ'.
    ○ ask for and accept a student's first name.
    ○ ask for and accept the student's GPA as a float.
    ○ test if the student's GPA is 3.5 or greater and, if so, print a message saying
        that the student has made the Dean's List.
    ○ test if the student's GPA is 3.25 or greater and, if so, print a message saying
        that the student has made the Honor Roll.
    • Test your app using at least five students.

Title: Student qualification
Developer: Padley Pérard
"""
# ask for and accept a student's last name.
student_lastname = input("Please enter your Last Name: ")

while (student_lastname != "ZZZ"):
    student_firstname = input("Please enter your First Name: ")
    student_GPA = float(input("What is your GPA? "))

    if (student_GPA >= 3.5):
        print(student_firstname, "You have made it to the Dean's List.")
    elif (student_GPA >= 3.25):
        print(student_firstname, "You have made it to the Honor Roll.")
    student_lastname = input("Please enter your Last Name: ")