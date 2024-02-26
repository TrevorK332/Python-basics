# Test 1 (Functions)

# Define a python function student(). Using
# function attributes display the names of
# all arguments.

def student(name):
    print(name)

student("John")
student("Arc")
student("Mark")
student("Alex")

# Test 2

# Write a python class named Student with two
# attributes student_name, marks. Modify the
# attribute values of the said class and print
# the original and modified values of the said
# attributes.

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

        def student_name(self):
            print(f'{self.student_name}')
        def marks(self):
            print(f'{self.marks}')
        def increment_marks(self):
            self.marks += 15
Student1 = Student("John", 420)
Student2 = Student("Arc", 400)
Student3 = Student("Mark", 421)
print(Student1.student_name)
print(Student1.marks)
print(Student2.student_name)
print(Student2.marks)
print(Student3.student_name)
print(Student3.marks)
Student1.increment_marks()
print(Student1.student_name)
print(Student1.marks)
Student2.increment_marks()
print(Student2.student_name)
print(Student2.marks)
Student3.increment_marks()
print(Student3.student_name)
print(Student3.marks)

# Test 3

# Write a python class called Rectangle
# constructed from the length and width and a method
# from the radius and two methods that will
# compute the area and perimeter of a circle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        def calculate_area(self):
            return self.length * self.width
        def calculative_perimeter(self):
            return self.length + self.width
area = Rectangle(8,3)
print("The area of the rectangle is", area.calculate_area())
perimeter = Rectangle(8, 3)
print("The perimeter of the rectangle is", perimeter.calculative_perimeter())

# Test 4

# Write a python class named circle, constructed
# from a radius and two methods that will compute
# the area and perimeter of a circle

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        def calculate_area(self):
            return math.pi * (self.radius ** 2)
        def calculative_perimeter(self):
            return 2 * self.radius * math.pi
circle = Circle(5)
area = circle.calculate_area()
print("The area of the circle is", circle.calculate_area())
perimeter = circle.calculative_perimeter()
print("The perimeter of the circle is", circle.calculative_perimeter())

#Test 5

import datetime
class BankAccount:
    def __init__(self, account_number, customer_name, opening_balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.opening_balance = opening_balance
        self.date_of_opening = datetime.datetime.now()
        def deposit(self, amount):
            if amount >0:
                self.balance += amount
                return True
            return False
        def withdraw(self, amount):
            if 0< amount <= self.balance:
                self.balance -= amount
                return True
            return False
        def check_balance(self):
            return self.balance
# Example usage
account = BankAccount(123456789, "Zack",1000.0)
print("Account Number:", account.account_number)
print("Customer Name:", account.customer_name)
print("Date of Opening:", account.date_of_opening.strftime("%Y-%m-%d"))
print("Balance:", account.check_balance())
# Deposit and check new balance
account.deposit(500.0)
print("Balance after deposit:", account.check_balance())
# Withdraw and check new balance
account.withdraw(200.0)
print("Balance after withdrawal:", account.check_balance)
