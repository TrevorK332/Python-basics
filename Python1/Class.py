class Person:
    name = 'John'
    age = 18
    gender = 'Male'
    maritial_status = 'Married'
print(Person.name)
print(Person.age)
print(Person.gender)
print(Person.maritial_status)

class Employees:
    firstname = 'Trevor'
    lastname = 'Nui'
    Salary = 145000
    gender = 'Male'
    age = 33
print(f'{Employees.firstname} {Employees.lastname} {Employees.Salary} {Employees.gender} {Employees.age}')
print(f'{Employees.firstname} {Employees.lastname} you are age is {Employees.age} and earn a salary of {Employees.Salary} and your gender is {Employees.gender}')
print(f'{Employees.firstname} {Employees.lastname} is a {Employees.gender} of age {Employees.age}')
# How to create one object in the parent class
class Parentx:
    firstname = 'Caroline'
    lastname = 'Smith'
Parent0 = Parentx()
print(Parentx.firstname)
print(Parentx.firstname)
# How to create more than one object in the parent class
class Parent:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
Parent1 = Parent('John','Steel', 35)
Parent2 = Parent('Alex','Smith', 45)
Parent3 = Parent('Ken', 'Bosco', 55)
print(Parent1.firstname)
print(Parent2.firstname)
print(Parent3.firstname)

class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
Cars1 = Cars('Ford', 'Ranger', 2000)
Cars2 = Cars('Toyota', 'Axis', 2014)
Cars3 = Cars('Nissan', 'Sunny', 1999)
print(Cars1.make)
print(Cars2.make)
print(Cars3.make)
print(f'My car model is {Cars1.make} {Cars1.model} from the year {Cars1.year}')
# Ford, Toyota and Nissan are all
# manufactured in year 1999
print(f'{Cars1.make}, {Cars2.make} and {Cars3.make} are all manufactured in the year {Cars3.year}')

# Create a class of students with three properties and
# derive three objects from it.
# Then display a paragraph

class students:
    def __init__(self, firstname, lastname, adm):
        self.firstname = firstname
        self.lastname = lastname
        self.adm = adm
students1 = students('Lizzie', 'Green', 13695)
students2 = students('Grey', 'Stone', 13696)
students3 = students('Trevor', 'Nui', 13698)
print(students1.firstname)
print(students2.firstname)
print(students3.firstname)
print(f'{students1.firstname} {students1.lastname} his admission is {students1.adm} and he is an A* student')
print(f'{students2.firstname} {students2.lastname} his admission is {students2.adm} and he is an C* student, and a trouble maker')
print(f'{students3.firstname} {students3.lastname} his admission is {students3.adm} and he is an E* student who misses classes')
# Use of method to print out the statement of the argument
class car:
    def __init__(self, make, model, price, year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
    def describe(self):
        print(f'My favourite car is {self.make} and it is a {self.model} model, built in the year {self.year} and it costs {self.price}')
obj1 = car('Ford', 'Ranger', 2000, 1999)
obj2 = car('Toyota', 'Axis', 3000, 2000)
obj3 = car('Nissan', 'Sunny', 4000, 2000)
obj1.describe()
obj2.describe()
obj3.describe()
print(obj1.describe())
print(obj2.describe())
print(obj3.describe())

class indiv:
    def __init__(self, firstname, lastname, gender, age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f'{self.firstname} {self.lastname}')
    def display_age(self):
        print(f'{self.age}')
    def display_gender(self):
        print(f'{self.gender}')
    def display_age1(self):
            print(f'{self.age}')
    def increment_age(self):
        self.age += 10

indiv1 = indiv('Lizzie', 'Green', 'Female', 22)
print(indiv1.fullname())
print(indiv1.display_age1())
indiv1.increment_age()
print(indiv1.increment_age())


