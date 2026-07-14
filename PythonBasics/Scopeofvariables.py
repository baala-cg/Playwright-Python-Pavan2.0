
#Global & Local variables
# The variables create outside of the function are called as Global variables.
# The variables create inside of the functions called as Local variables.

#Example 1:
#
# x=20  # global variable
#
# def myfun():
#     y=10 # local variable
#     #print(x)  # 20 able to access global variable within the function
#     #print(y) # 10
#
# myfun()
#
# # print(x)  #20
# # print(y) # type error , cannopt access local variable in outside of the function


# Example 2: same name for global and local variables
#
# x=100  # global varaible
#
# def myfun():
#     x=200  # local varaible
#     print(x) # 200
#
# myfun()
#
# print(x) #100


#Example 3: Using Global variable in Local variable and update value
# x=100  # global varaible
#
# def myfun():
#     global x
#     x=200
#     print(x) #200
#
# myfun()
#
# print(x)  #200




#Example 4: Declare the Global variable inside the function
#There is no need to declare global variables outside the function.
#You can declare them global variables inside the function - using global keyword


def myfun():
    #global x=100   # syntax errror - not valid
    global x
    x=100
    print(x)


myfun()

print(x) # 100 able to access x bcoz it is global variable