# lists
my_list = [123,276,312,476,512]
print(my_list)
print(my_list[4])
print(my_list[0])
print(my_list[2])
print(my_list[1:4])
my_list[0] = 132
print(my_list)
print(len(my_list))
my_list.append(345)
print(my_list)
my_list.insert(1,254)
print(my_list)
my_list.insert(4, 213)
print(my_list)
my_list.extend([123,276,312])
print(my_list)
# If you want to remove a value from your list?
# 1) Method1
my_list.remove(312)
print(my_list)
# 2) Method2
del my_list[2]
print(my_list)
print(len(my_list))
# 3) Method3
my_list.clear()
print(my_list)
del my_list
my_list2 = [123,265,389,412,509]
print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))
print(sum(my_list2)/len(my_list2))
# Knowing the index position
my_list2.index(123)
print(my_list2)
# Create a list of 5 student names.
# Append one more student using the
# function, delete the first value of the list,
# then clear the list
my_list3 = [John,James,Trevor,Ken,Jude]
