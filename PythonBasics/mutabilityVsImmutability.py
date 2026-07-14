# Mutability vs. Immutability
# Mutable object → Can be changed after creation. (e.g., list, dict, set)
# Immutable object → Cannot be changed after creation. (e.g., int, float, tuple, str)

#Example1

# s1="hello"
# print("original string :", s1) #hello
# print("Address: ",id(s1))  #2541334803248
#
# #print(s1[0])  #h
# #s1[0]= "H"  # String is immutable so we cannot change the value
#
# # Hello
# s1="H"+s1[1:]
#
# print(s1)
# print(id(s1))
#

#Example 2:

# s1="python"
# #s2=s1.replace("p", "P")
#
# print("Before replace:", id(s1))
# s1=s1.replace("p", "X")
# print("After replace:", id(s1))
#
# print(s1)
# #print(s2)
# print(s1)


#   Example 3

mylist=["h","e","l","l","o"]
print("original list:", mylist) #['h', 'e', 'l', 'l', 'o']
print("before modification id id:",id(mylist))
mylist[0]="H"
print("after modification:", mylist)  # mutable
print("after modification id is:", id(mylist))











