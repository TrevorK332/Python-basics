# Forloop in lists
number = [234,768,989,979,4343]
for i in number:
    print(i)
# Forloop in set
set = ['Eric','Tim','Palmer','Doku']
for name in set:
    print(name)

my_string = "Hello world , welcome to my channel"
for letter in my_string:
    print(letter)



char = ("a","b","c")
for letter in char:
    if letter == "b":
        continue
    print(letter)
else:
    print("Finished")
