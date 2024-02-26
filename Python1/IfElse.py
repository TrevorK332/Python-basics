# Conditional statements with if and else #
# Example 1
age = int(input("How old are you? "))
if age >= 18:
   print("You are old enough to move out")
   print("You are old enough to have an ID")
else:
   print("You are not old enough to move out")
   print("You are not old enough to have an ID")
# Example 2
marks = float(input("Enter your marks"))
if marks >=90 and marks <=100:
      print("You have an A*")
elif marks >=80 and marks <=89:
      print("You have an A")
elif marks >=70 and marks <=79:
      print("You have an B")
elif marks >=60 and marks <=69:
      print("You have an C")
elif marks >=50 and marks <=59:
      print("You have an D")
elif marks >=40 and marks <=49:
      print("You have an E")
elif marks >=20 and marks <=39:
      print("You have an F")
elif marks >=0 and marks <=19:
      print("You have an U")
else:
     print("Enter valid marks")
# Example 3
age1 = int(input("How old are you? "))
if age1 >= 65:
   print("You are old enough to retire")
elif age1 < 65 and age1 >= 50:
   print("You are almost going to retire")
elif age1 < 50 and age1 >= 40:
   print("You are still active")
elif age1 < 40 and age1 >= 18:
   print("You are considered youthful")
else:
   print("You are still young")


# Create a program that takes in human temperature in celcius and performs
# certain tasks. If the temperature in above 30, tell the user
# to have a vest on, if between 20 and 30 the user should put on a sweater and if below
# tell the user to pit on jacket

Temperature = float(input("Enter your Temperature"))
if Temperature > 30:
      print("Put on a Vest")
elif Temperature > 20 and marks < 30:
      print("Put on a Sweater")
elif Temperature < 20:
      print("Put on a Jacket")
else:
     print("Enter valid marks")

# Take in the height and weight of a person as
# inputs. Let the height be in meters and weight be
# in kilograms perform BMI calculations using the two inputs
# above. Now create a conditional statement to
# categorize the person using he/her BMI as
# follow. If BMI is below 18 then display,
#
weight = float(input("Enter weight in kilograms : "))
height = float(input("Enter height in meters : "))

BMI = weight/(height+height)
print(BMI)

if BMI <=18:
    print('You are under weight')
elif BMI <18 and BMI >=25:
    print('You are normal')
elif BMI < 25 and BMI >=30:
    print('You are overweight')
elif BMI < 30 and BMI >=100:
    print('You are obese')
else:
    print('Enter valid values')