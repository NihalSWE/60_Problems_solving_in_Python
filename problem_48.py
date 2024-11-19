# Exercise 48  : Student class 

# Write  a Python class called "Student" with the following members:
# name: (of type char),
# grade1, grade2: (of type float)
# calc_avg(): calculates the average grade.
# display(): displays the name and average grade.
# The main program asks the user to enter a student's name and grades. and displays their name and average grade.

class Student:
    def __init__(self, name, grade1, grade2):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
    def calc_avg(self):
        return (self.grade1 + self.grade2) / 2
    def display(self):
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.calc_avg()}")

name=input('Enter Your Name: ')
grade1=float(input('Enter Your First Grade: '))
grade2=float(input('Enter Your Second Grade: '))
s1=Student(name,grade1,grade2)
s1.display()