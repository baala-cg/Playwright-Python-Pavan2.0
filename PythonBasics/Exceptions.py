
#Example 1:

# print("welcome"   # causing the error

#Example 2: Exception

# n=10
# res=n/0  #ZeroDivisionError: division by zero
# print(res)

#Example 3:

#x="10"
#x=int("10") #Type Error
# x=int("wel") #ValueError:
# print(x+5)


#Example 4: Handling exceptions using   try &  except

# print("started....")
# print(x) #NameError: name 'x' is not defined
# print("finished....")


# print("started....")
# try:
#     print(x)
# except:
#     print("An exception occured..")
# print("Finished...")


#Example 5:  many exceptions ( we can define multiple exceptions for single try

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined.")
# except:
#     print("Some other exception..")


#Example 6: else with try

#  We can use the else keyword to define a block of code to be executed if no errors were raised

# try:
#     #print("Hello")
#     100/0
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")



#Example 7: finally

# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# try:
#     #print(x)
#     #print("welcome")
# except:
#     print("Something went wrong")
# finally:
#     print("this is finally block...")


#Example 8: try, except, else, finally
# 0  - ZeroDivisionError
# xyx - ValueError
# 2

# try:
#     n=int(input("Enter a value:"))
#     res=100 / n
# except ZeroDivisionError :
#     print("You can't divide by Zero..")
# except ValueError:
#     print("Enter a valid number..")
# else:
#     print(res)
# finally:
#     print("Exceptions completed......")


#Example 9: try inside another try

# try:
#     file=open("C:/Automation/automationFiles/myfile.txt","r")
#     try:
#         file.write("welcome")
#     except:
#         print("Something went wrong when writing data into file")
#     finally:
#         file.close()
# except:
#     print("Something went wrogn when opening the file...")


#Example 10 : Raise exceptions

# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the 'raise' keyword.

# x=-1
#
# if x<0:
#     raise Exception("Sorry.. no numbers below zero..")


#Example 11 :You can define what kind of error to raise,

# x="hello"
#
# if not type(x) is int:
#     raise TypeError("Only integers are allowed..")
#


#Example 12: how the developer raise exceptions


def set(age):
    if age<0:
        raise ValueError("Age cannot be negative..")
    print("Age is set", age)


# usage

# set(20) # valid


try:
    set(-10) # invalid
except ValueError:
    print("invalid data provided....")








































