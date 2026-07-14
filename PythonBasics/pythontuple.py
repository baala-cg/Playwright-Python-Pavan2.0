# creating tuple

# mytuple=("apple","banana","cherry")
# print(mytuple)  #('apple', 'banana', 'cherry')


#Access tuple elements/values
# mytuple=("apple","banana","cherry")
# print(mytuple[0])  # apple
# print(mytuple[-1])  # cherry

#count number of times value is repeated
# mytuple=("apple","banana","cherry","apple","apple")
# print(mytuple.count("apple"))  #3

# range of indexes
# mytuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1]) #('orange', 'kiwi', 'melon')


# change the values in a tuple
# by default tuple does not allow you change values bcoz it is immutable
# but there is work around

# tuple--->list--->tuple
#
# mytuple=("apple", "banana", "cherry")
# #mytuple[1]="orange"   # not possible to change
#
# mylist=list(mytuple)
# print("after converting into list:", mylist) #['apple', 'banana', 'cherry']
# mylist[1]="orange"
# print("after changing mylist is:", mylist) #['apple', 'orange', 'cherry']
#
# mytuple=tuple(mylist)
# print(mytuple) #('apple', 'orange', 'cherry')


# retrive the data from tuple usign looping statement
#mytuple=("apple","banana","cherry")

# for i in mytuple:
#     print(i)

# item exist or not ( searching an item in tuple)

#mytuple=("apple","banana","cherry")

#print("cherry" in mytuple)  # True

# if "cherry" in mytuple:
#     print("exists")
# else:
#     print("not exists")


# length - count number of values ina tuple
# mytuple=("apple","banana","cherry")
# print(len(mytuple))  #3


# Adding new values  - not possible bcoz tuple is immutable
#mytuple=("apple","banana","cherry")
#mytuple[3]="orange"   # invalid/incorrect cannot add new value  TypeError:


#Copying the tuple
# mytuple1=("apple","banana","cherry")
# mytuple2=mytuple1
# print(mytuple2)   #('apple', 'banana', 'cherry')


# Remove the values from tuple -- not possible bcoz tuple is immutable
# mytuple=("apple","banana","cherry")
# mytuple.remove("apple")  # incorrect/invalid


# joining the tuples
tuple1=("a","b","c")
tuple2=(10,20,30)
tuple3=tuple1+tuple2
print(tuple3)  # ('a', 'b', 'c', 10, 20, 30)










