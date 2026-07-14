
# creating set
# myset1={10,20,30,40,50}
# myset2={"apple","banana","cherry"}
# myset3={100,"A", True,"welcome"}
# myset=set()  # this is empty set
#
#
# print(myset1) # {50, 20, 40, 10, 30}
# print(myset2) #{'apple', 'cherry', 'banana'}
# print(myset3) #{'A', 'welcome', 100, True}
# print(myset)  #set()


# Access the values from a set

# You cannot access items in a set by referring to an index(bcoz set does not support index).

# you cannot even change the  items, but you can add new items to set.(bcoz set does not support index)

# Access data from set using for loop

# myset={'apple', 'cherry', 'banana'}
#
# for i in myset:
#     print(i)


# check if teh value exist ( searching item/value in teh set)
# myset={'apple', 'cherry', 'banana'}
#
# print("apple" in myset)  # True
# print("orange" in myset)  # False
#
# if "apple" in myset:
#     print("exist")
# else:
#     print("not exist")

# find lenght / number of values in a set
# myset={'apple', 'cherry', 'banana'}
# print(len(myset))  # 3


# count number of times value is repeated in the set
# - Not possible, since set not allowed duplicates

# Sorting the set
# - Not possible , since set is unordered

# Reversing set items
# - Not possible , since set is unordered


# Add items/values into set
# add()  - we can add single value
#update() - we can add multiple values
# - Not possible insertion since set is unordered and not supported index

#
# myset={'apple', 'cherry', 'banana'}
#
# # myset.add("orange")
# # print("After adding:", myset)  #{'apple', 'banana', 'orange', 'cherry'}
#
# myset.update(["mango","grapes"])
# print(myset)  #{'banana', 'apple', 'mango', 'cherry', 'grapes'}


# if you have duplicates in a set it will ignore
# myset={1,2,3,4,5,1,2,3}
# print(myset) #{1, 2, 3, 4, 5}  # duplicate values are ignored


# Remove items/values from a set

#Appraoch 1 : using remove()

# myset={"apple","banana","cherry"}
# #myset.remove("cherry")
# #myset.remove("xyz")  # KeyError:   if the value is not exist in the set
# print("after removing :", myset)  # {'banana', 'apple'}


# Appraoch 2: using discard()
# myset={"apple","banana","cherry"}
# #myset.discard("cherry")
# #myset.discard("xyz")  # will not throw any error if teh value is not exists
# print("after removing :", myset)  #{'apple', 'banana'}

# Appraoch 3 : pop() :removes a random item/value from the set.

# myset={"apple","banana","cherry"}
# myset.pop()
# print("after removing :", myset)  # {'cherry', 'banana'}


# clearing values from a set

# myset={"apple","banana","cherry"}
# myset.clear()
# print("after clearing:", myset) #  set()

# delete set
# del myset
# print("After deletion:",myset)  #NameError:


# Copying set

#Appraoch 1: copy()
# myset1={"apple","banana","cherry"}
# myset2=myset1.copy()
#
# print(myset1) #{'banana', 'apple', 'cherry'}
# print(myset2) #{'banana', 'apple', 'cherry'}


# Appraoch 2: set()

# myset1={"apple","banana","cherry"}
# #myset2=myset1
# myset2=set(myset1)
#
# print(myset1)
# print(myset2)


# Joining of sets


# Appraoch1 :   using union()

# myset1={"a","b","c"}
# myset2={10,20,30}
# myset3=myset1.union(myset2)
#
# print(myset3)  # {'a', 'c', 20, 'b', 10, 30}


# Apprach 2 : using  |  symbol
# myset1={"a","b","c"}
# myset2={10,20,30}
# myset3=myset1 | myset2
#
# print(myset3)  # {'a', 20, 10, 'c', 30, 'b'}



# Retreivng common values from 2 sets
# intersection()

# #Appraoch 1:  intersection()
#
# myset1={"a","b","c",10}
# myset2={10,20,30,"a"}
#
# myset3=myset1.intersection(myset2)
# print(myset3) # {'a', 10}


#Appraoch 2:  using  & symbol

myset1={"a","b","c",10}
myset2={10,20,30,"a"}

myset3=myset1 & myset2
print(myset3) # {'a', 10}

















