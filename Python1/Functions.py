# Function
print('This is my function')
print('This is my function')
print('This is my function')

def my_function():
    print('This is my function')
    print('This is my function')
    print('This is my function')
my_function()
my_function()
# How to add an argument inside the function ()
def my_function01(name):
    print(name)
    print(name)
    print(name)
my_function01('Trevor')
my_function01('Terrence')
my_function01('Timothy')


def num(numbers):
    print(numbers)
    print(numbers)
num(56)
num(23)
# concatination

def salutations(first_name):
    print('Hello' + first_name + 'Good Morning')
salutations(' Esther ')
salutations(' Ann ')

def miaka(age):
    print('Hello, you are ' + str(age) + ' years')
miaka(18)


def my_name(first_name1, last_name1):
    print(first_name1 + ' ' + last_name1 + "is this a student")
# How to display age using three arguments
def sentence(firstname, lastname, age1):
    print(firstname + lastname + ' ' + ' is' + str(age1) + 'years old')
sentence('John', ' Ann ', 16)
# How to add conditional statements to functions
def employees(firstnames01, age01):
    if age01 >=20:
        print(firstnames01 + ' you are' + str(age01) + 'years old')
    elif age01 <20 and age01 >=15:
        print(firstnames01 + ' you are' + str(age01) + 'years old')
    elif age01 <15 and age01 >=10:
        print(firstnames01 + 'you are' + str(age01) + 'years old')
    else:
        print(firstnames01 + 'you are' + str(age01) + 'you are young')

employees('Trevor', 20)

def age_calculator(Birth_Year):
    Current_Year = float(input("Enter the current year : "))
    Birth_Year = float(input("Enter the birth year : "))
    age00 = Current_Year - Birth_Year
    return age00
print(age_calculator(2))

def marks_calculator(*subjects):
    total_marks = sum(subjects)
    return total_marks
print(marks_calculator(23,45,67))
print(marks_calculator(2,56,68,90))
print(marks_calculator(34,56))

# Create a function that takes three arguments
# one is a string and two are integers; calculate
# the totals of the integers and display the output

def v(subject,number,variable):
    totals = subject + str(number+variable) + ' are your totals'
    return totals
print(v('English', 45, 48))

# Create a function that takes in location and age
# arguments. Then perform conditional statements
# as below;
# above 60 post them to kisumu
# 50-60 post them to nakuru
# 30-40 post them to mombasa
# others to be posted to nairobi

def l(location,age3):
    if age3 >=60:
        print('you are posted to Kisumu')
    elif age3 <60 and age3 >=50:
        print('you are posted to Nakuru')
    elif age3 < 50 and age3 >= 40:
        print('you are posted to Mombasa')
    elif age3 <40 and age3 >=30:
        print('you are posted to Nairobi')
    else:
        print('Was good cuz')
l('Nairobi', 60)
l('Muranga', 55)
l('Nairobi',  12)
# Additional work
def country(nchi = 'Kenya'):
    return nchi
print(country("Tanzania"))
print(country("Uganda"))
print(country("Russia"))
print(country())
