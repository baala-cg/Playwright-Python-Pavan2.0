# 1. Arbitrary or Variable-length Arguments
# 2. Positional or Required Arguments
# 3. Keyword Arguments

# Example 1 : Function with Arbitrary or Variable-length Arguments

# def sum_function(*numbers):
#    total =0
#    for i in numbers:
#        total=total+i
#    return total
#
#
# print(sum_function(10,20)) #30
# print(sum_function(10,20,30)) #60
# print(sum_function(100,200,300)) #600
# print(sum_function()) #0



# Example 2 : Function with positional and keyword arguments

# def myfun(i,j):
#     print(i,j)

#myfun(10,20)  # positional arguments

#myfun(i=10,j=20)  # keyword arguments
#myfun(j=10,i=20)  # keyword arguments



#Example 3: Default values can be assigned to positional arguments
# def myfun(i=10,j=20):
#     print(i,j)
#
# myfun(100)  # 100 20
# myfun()  #10 20



#Example 4: Mixing of both the positional and keyword arguments

# def myfun(a,b,c):
#     print(a,b,c)

# myfun(10,20,30)  # positional argumnets

#myfun(a=10,b=20,c=30)  # keyword argumnets
#myfun(c=10,b=20,a=30)  # keyword arguments

#myfun(10,20,c=30)  #10 20 30
#myfun(10,b=20,c=30)  #10 20 30

#myfun(10,b=20,30) #this is wrong as positional argument must appear before any keyword argument
#myfun(10,30,b=20)  # this is having logical error


#Example 5: Function can return multiple values

# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
#
#
# #print(largest(100,200))  # (200, 100)
#
# res=largest(100,200)
# print(res) #(200, 100)
#
# print(type(res)) #tuple

























