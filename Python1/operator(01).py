# Assigned operators
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print(first+second)
print(first-second)
print(first*second)
print(first/second)
print(first**second)
print(first//second)
#
# x = 2
# x = x+1 or x+=1
# x = x-1 or x-=1
# x = x*2 or x*=3
# x = x/2 or x/=2

c = input("Enter a number: ")
d = input("Enter another number: ")
print(c==d)
print(c<=d)
print(c>=d)
print(c!=d)
print(c>d)
print(c<d)
# Logical operators
y = 4
p = 6
print((p>y) or (p<y))
print((p<y) or (p>y))
print((p>=y) or (p<=y))
print((p<=y) or (p>=y))
print((p==y) or (p==y))
print((p>y) and (p<y))
print((p<y) and (p>y))
print((p>=y) and (p<=y))
print((p<=y) and (p>=y))
print((p==y) and (p==y))
print(not ((p==y) and (p==y)))


# identical operators
a = 10
b = "string"
result = a is b
print(result)
result1 = a is not b
print(result1)
result2 = type(a) is type(b)
print(result2)
result3 = type(a) is not type(b)
print(result3)

first_int = float(input("Enter first number: "))
second_int = float(input("Enter second number: "))
addition = first_int + second_int
print("first_int: " + str(second_int))
subtraction = first_int - second_int
print("first_int: " + str(second_int))
# x = x+3 x+=3
# subtraction = subtraction + 3

print((addition>subtraction) or (addition<subtraction))
print((addition<subtraction) and (addition>subtraction))
print((subtraction>addition))
print((subtraction<addition))

# create a program that takes three input
# numbers from user. Declare one variable
# with an integer then add a 7 to one of
# the input using assignment operators.
# Perform multiplication of the first two
# inputs then store in a variable, perform
# division of one input and the variable.
# Lastly perform logical operations

w = float(input("Enter first number: "))
s = float(input("Enter second number: "))
d = float(input("Enter third number: "))