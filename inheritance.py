import sys
import math
from collections import defaultdict, deque
from functools import lru_cache

'''Problem Statement
   Design a system to manage different types of people at a university, such as students, teachers, and staff members.
   Each type of person shares common attributes and behaviors but also has specific characteristics and actions.'''

class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

class Student(Person):
    def __init__(self,name,age,address,student_id,course,grades):
        super().__init__(name,age,address)
        self.student_id = student_id
        self.course = course
        self.grades = grades

    def display_details(self):
        return f"{super().display_details()},Student ID: {self.student_id}, Course: {self.course}, Grades: {self.grades}"

    def calculate_gpa(self):
        return sum(self.grades)

class Teacher(Person):
    def __init__(self, name, age, address, employee_id, department, subjects):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.department = department
        self.subjects = subjects
    
    def display_details(self):
        return f"{super().display_details()}, Employee ID: {self.employee_id}, Department: {self.department}, Subjects:{self.subjects}"
    
    def teach(self):
        return f"{self.name} is teaching {','.join(self.subjects)}."

class Staff(Person):
    def __init__(self, name, age, address, staff_id, position):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.position = position
        
    def display_details(self):
        return f"{super().display_details()}, Staff ID: {self.staff_id}, Position: {self.position}"

    def work(self):
        return f"{self.name} is working as a {self.position}."

    

def main():
    #Input handling

    # input_data = sys.stdin.read
    # data = input_data.split()
    
    # Create instances of each class
    student = Student("Alice", 20, "123 Main St", "S123", "Computer Science", [90, 85, 88, 92])
    teacher = Teacher("Bob", 45, "456,Elm St", "T456", "Mathmatics", ["Calculus", "Algebra"])
    staff = Staff("Charlie", 35, "789 Oak St", "ST789", "Administrtor")

    # Display details and specific behaviors

    print(student.display_details())
    print(f"GPA: {student.calculate_gpa()}\n")

    print(teacher.display_details())
    print(teacher.teach(),"\n")

    print(staff.display_details())
    print(staff.work())

    # Example of reading integerfrom input
    # num_cases = int(data[0])
    # index = 1


    # Example processing loop
    # for _ i in rande(num_cases):
        #   n = int(data[index])
        #   index += 1
        #   Process the input data
        #   result = some_function(n)
        #   print(result)

def some_function(x):
    # Example function for processing
    return x*x

if __name__ == "__main__":
    main()
