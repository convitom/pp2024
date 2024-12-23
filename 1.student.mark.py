# Student Mark Management System

# Input functions
def input_number_of_students():
    return int(input("Enter number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def input_marks_for_course(students, course_name):
    print(f"Input marks for course: {course_name}")
    marks = {}
    for student in students:
        student_id = student[0]
        mark = float(input(f"Enter marks for {student[1]} (ID: {student_id}): "))
        marks[student_id] = mark
    return marks

# Listing functions
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks(course_marks, students):
    print("Marks:")
    for student_id, mark in course_marks.items():
        student_name = next(student[1] for student in students if student[0] == student_id)
        print(f"Student: {student_name} (ID: {student_id}), Mark: {mark}")


