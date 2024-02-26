# Sets
my_set = {122,234,3455,445,52}
print(my_set)
# How to add more values
my_set.add(234)
print(my_set)
my_set.update([2432,3453,3453])
print(my_set)
# How to copy your old set into your new one
my_set2 = my_set.copy()
print(my_set2)
print(len(my_set))
my_set.discard(234)
print(my_set)
# How to delete your set
my_set.clear()
print(my_set)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))
# Use of conditional statements
names = {"John","Andrew","Peter","Smith"}
if "Andrew" in names:
    print('Student is present in the school system')
else:
    print('>= is not present in the school system')
# How to use a conditional value to print one value in a set
Parents = {'Mark','Joe','Peter','Lois','Chris'}
one_value = "Peter"
if one_value in Parents:
    output = one_value
    print(output)

# Create a set of integers and floats value
# then perform conditional statements to check their
# presence in that set
my_set3 = {'Mark',231,'Joe',66}
if "Joe" in names:
    print('This is in the set')
else:
    print('This is not in the set')