# Dictionary
my_dictionary = {
    "Name": "Trevor",
    "Gender": "Male",
    "Age": 20,
    "Marital Status": "Single",
}
print(my_dictionary)
print(my_dictionary['Name'])
print(my_dictionary['Gender'])
print(my_dictionary['Age'])
print(my_dictionary['Marital Status'])
print(my_dictionary.get('Gender'))
# How to change marital/age/gender status
my_dictionary['Marital Status'] = "Married"
print(my_dictionary)
my_dictionary['Age'] = "28"
print(my_dictionary)
my_dictionary['Gender'] = "Female"
print(my_dictionary)
# How to include important data that was missed
my_dictionary['Location'] = "Nairobi"
print(my_dictionary)
my_dictionary['Salary'] = "$125000"
print(my_dictionary)
# How to copy your old dictionary into your new one
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))
print(len(my_dictionary2))
# How to get rid of specific data
my_dictionary2.pop("Marital Status")
print(my_dictionary2)
my_dictionary2.pop("Gender")
print(my_dictionary2)
my_dictionary2.pop("Age")
print(my_dictionary2)
del my_dictionary2["Location"]
print(my_dictionary2)
# How to delete your dictionary
del my_dictionary
print(my_dictionary2)
my_dictionary3 = {
    "Name": "Mark",
    "Gender": "Male",
    "Age": 37,
    "Job": "Software Engineering",
    "Salary": "$125000",
    "Ethnicity": "White",
    "Location": "Germany",
    "Marital Status": "Single",
}
print(my_dictionary3)