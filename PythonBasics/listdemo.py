# creating list

# mylist1=[10,20,30,40,50]
# mylist2=["apple","mango","cherry"]
# mylist3=[10,"apple","A", True]
#
# mylist4=list()  # this will create emtpy list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4)  # []


# Access items/values/objects
# mylist=["apple","banana","cherry"]   # index starts from zero 0
#
# print(mylist[0]) # apple
# print(mylist[2]) # cherry
#
# print(mylist[-1])  # cherry
# print(mylist[-2])  #banana


# Access multiple values from a list ( range of indexes)
# mylist=["apple","banana","cherry","orange","kiwi","melon", "mango"]
#
# print(mylist[2:5]) #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])  #['orange', 'kiwi', 'melon']


# change the item value in list
# mylist=["apple", "banana", "cherry"]
# print("Before change:",mylist)  # ['apple', 'banana', 'cherry']
# mylist[0]="orange"
# print("After the change:",mylist)  #['orange', 'banana', 'cherry']


# # loop with list
# mylist=["apple","banana","cherry"]
#
# for i in mylist:
#     print(i)


# check if the item is exist or not ( Searching an item in a list)
# mylist=["apple","banana","cherry"]
#
# if "banana" in mylist:
#     print("Yes, banana is exist")
# else:
#     print("No, banana is not exist")



# find out length/size of a list

# str="welcome"
# print(len(str)) # 7
#
# mylist=["apple","banana","cherry"]
# print(len(mylist))  #3


# count number of times value is repeated in the list
# mylist=["apple","banana","cherry","apple","apple"]
# print(mylist.count("apple"))  # 3

# sorting the list
#
# mylist = ['cherry','mango', 'banana','apple']
#
# print("original list:",mylist)
# #mylist.sort()  # sort the elements ascending order  ['apple', 'banana', 'cherry', 'mango']
# mylist.sort(reverse=True) # sort the elements in descending order ['mango', 'cherry', 'banana', 'apple']
# print("Sorted values:", mylist)


# Reversing list items
# pre-requisite: values must be in sorted order
#
# mylist = ['apple', 'banana', 'cherry', 'mango']  # asceding order
# print("original values:", mylist)
# mylist.reverse()
# print("reversed values in a list:", mylist)  # ['mango', 'cherry', 'banana', 'apple']


# Add item   append()   insert()

# mylist=["apple", "banana", "cherry"]
# print("before append:", mylist) #['apple', 'banana', 'cherry']
# mylist.append("orange")
# print("after append:", mylist) #['apple', 'banana', 'cherry', 'orange']
#
# mylist=["apple", "banana", "cherry"]
# print("Before insertion:", mylist)  #['apple', 'banana', 'cherry']
# mylist.insert(1,"orange")
# print("After insertion:", mylist) #['apple', 'orange', 'banana', 'cherry']


# remove item from the list

# Appraoch 1:  remove()  accepts value
# mylist=["apple", "banana", "cherry"]
# mylist.remove("banana")
# print("After removing:", mylist) #['apple', 'cherry']

# Approach 2 : pop()   accepts index
# mylist=["apple", "banana", "cherry"]
# mylist.pop(2)
# print("after removing:", mylist)  #['apple', 'banana']


# Approach 3: del
# mylist=["apple", "banana", "cherry"]
# del mylist[1]  # we passed index of the element, here del is not a method,, it is a identifier/keywork
# print(mylist) # ['apple', 'cherry']


#deleting the list
# del
# mylist=["apple", "banana", "cherry"]
# del mylist
# print(mylist)


# Copying the list

# Approach 1:  copy()

# mylist1=["apple", "banana", "cherry"]
# mylist2=mylist1.copy()
#
# print(mylist1)
# print(mylist2)


# Appraoch 2: list()
# mylist1=["apple", "banana", "cherry"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)


# Join the lists

# Approach 1: using +

# list1=["a","b","c"]
# list2=[1,2,3]
#
# list3=list1+list2
# print(list3)


# Appraoch 2: using for loop
list1=["a","b","c"]
list2=[10,20,30]
list3=list()


# for i in list2:
#     list1.append(i)
#
# print(list1)  #['a', 'b', 'c', 10, 20, 30]


for i in list1:
    list3.append(i)

for i in list2:
    list3.append(i)

print(list3)

#Appraoch3 : using extend() method
# list1=["a","b","c"]
# list2=[10,20,30]
# list1.extend(list2)
# print(list1) #['a', 'b', 'c', 10, 20, 30]

















































































