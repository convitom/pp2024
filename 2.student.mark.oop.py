import math
import numpy as np
import curses

# Student Mark Management System (OOP Version)

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, Date of Birth: {self.__dob}, GPA: {self.__gpa:.1f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"ID: {self.__course_id}, Name: {self.__name}, Credits: {self.__credits}"


class Marks:
    def __init__(self, course):
        self.__course = course
        self.__marks = {}

    def input_marks(self, students):
        print(f"Input marks for course: {self.__course.get_name()}")
        for student in students:
            mark = float(input(f"Enter marks for {student.get_name()} (ID: {student.get_id()}): "))
            rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            self.__marks[student.get_id()] = rounded_mark

    def get_marks(self):
        return self.__marks

    def show_marks(self, students):
        print(f"Marks for course: {self.__course.get_name()}")
        for student_id, mark in self.__marks.items():
            student_name = next(student.get_name() for student in students if student.get_id() == student_id)
            print(f"Student: {student_name} (ID: {student_id}), Mark: {mark}")


class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.__students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            course = Course(course_id, name, credits)
            self.__courses.append(course)
            self.__marks[course_id] = Marks(course)

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self.__courses if c.get_id() == course_id), None)
        if course:
            self.__marks[course_id].input_marks(self.__students)
        else:
            print("Invalid course ID.")

    def calculate_gpa(self):
        for student in self.__students:
            total_credits = 0
            weighted_sum = 0
            for course in self.__courses:
                course_id = course.get_id()
                if course_id in self.__marks:
                    marks = self.__marks[course_id].get_marks()
                    if student.get_id() in marks:
                        weighted_sum += marks[student.get_id()] * course.get_credits()
                        total_credits += course.get_credits()
            if total_credits > 0:
                gpa = weighted_sum / total_credits
                student.set_gpa(math.floor(gpa * 10) / 10)  # Round down to 1 decimal place

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_students(self):
        print("Students:")
        for student in self.__students:
            print(student)

    def list_courses(self):
        print("Courses:")
        for course in self.__courses:
            print(course)

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        if course_id in self.__marks:
            self.__marks[course_id].show_marks(self.__students)
        else:
            print("Invalid course ID.")

    def menu(self, stdscr):
        curses.wrapper(self.__menu)

    def __menu(self, stdscr):
        stdscr.clear()
        while True:
            stdscr.addstr(0, 0, "Options:")
            stdscr.addstr(1, 0, "1. List courses")
            stdscr.addstr(2, 0, "2. List students")
            stdscr.addstr(3, 0, "3. Input marks for a course")
            stdscr.addstr(4, 0, "4. Show student marks for a course")
            stdscr.addstr(5, 0, "5. Calculate GPA and Sort Students")
            stdscr.addstr(6, 0, "6. Exit")
            stdscr.addstr(7, 0, "Enter your choice: ")
            stdscr.refresh()

            choice = stdscr.getstr(7, 20, 2).decode('utf-8')

            if choice == '1':
                stdscr.clear()
                stdscr.addstr(0, 0, "Courses:")
                for course in self.__courses:
                    stdscr.addstr(f"{course}\n")
            elif choice == '2':
                stdscr.clear()
                stdscr.addstr(0, 0, "Students:")
                for student in self.__students:
                    stdscr.addstr(f"{student}\n")
            elif choice == '3':
                stdscr.clear()
                self.input_marks()
            elif choice == '4':
                stdscr.clear()
                self.show_marks()
            elif choice == '5':
                self.calculate_gpa()
                self.sort_students_by_gpa()
                stdscr.clear()
                stdscr.addstr(0, 0, "Students sorted by GPA:")
                for student in self.__students:
                    stdscr.addstr(f"{student}\n")
            elif choice == '6':
                break
            else:
                stdscr.clear()
                stdscr.addstr(0, 0, "Invalid choice, please try again.")
            stdscr.refresh()

if __name__ == "__main__":
    system = ManagementSystem()
    system.input_students()
    system.input_courses()
    curses.wrapper(system.menu)
