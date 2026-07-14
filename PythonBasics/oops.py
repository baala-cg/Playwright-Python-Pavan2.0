#Example 1: Creating a class along with object

# class Myclass:
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print(name)
#
# mc1=Myclass()
# mc1.myfun()
# mc1.display("John")
#
# mc2=Myclass()
# mc2.myfun()
# mc2.display("Scott")




# Example 2: Instance Method Vs static method
##   Note: 'self' inside the static method is just a parameter name, it doesn’t refer to object.

# class Myclass:
#     def m1(self):
#         print("this is instance method...")
#
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# # mc=Myclass()
# #
# # mc.m1()   # instance method
# # mc.m2(10,20)  # static method
#
# Myclass.m2(10,20)  # static methods can be access directly from teh class
#


#Example 3: define the variables inside the class ( class variables/ instance variables)
#
# class Myclass:
#     a,b=10,20 # class variables
#
#     def add(self):
#         print(self.a+self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add() # 30
# mc.mul()  #200



#Example 4: Local variables, Global variables & Class variables

# i,j=15,25   # Global varaibles
#
# class Myclass:
#     a,b=10,20   # Class varaibles
#
#     def add(self,x,y):
#         print(x+y)   # local varaibles   #300
#         print(self.a+self.b)  # class varaibles #30
#         print(i+j)  # Global variables  # 40
#
# mc=Myclass()
# mc.add(100,200)



#Example 5: Local variables, Global variables & Class variables  ( names of varaibles are same)
# a,b=15,25   # Global varaibles
#
# class Myclass:
#     a,b=10,20   # Class varaibles
#
#     def add(self,a,b):
#         print(a+b)   # local varaibles   #300
#         print(self.a+self.b)  # class varaibles #30
#         print(globals()['a']+globals()['b'])  # Global variables  # 40
#
# mc=Myclass()
# mc.add(100,200)



#Example 6: Class with constructor
#  __init__(self)  : constructor
# constructor used for initilize data
# constructor invoked automatically when object is created.

# class Myclass:
#     def __init__(self):
#         print("This is constructor..")
#     def m1(self):
#         print("Hello...")
#     def m2(self,x,y):
#         return x+y
#
# mc=Myclass()
#
# mc.m1()
# print(mc.m2(10,20))


# Example 7: Constructor with parameters and class varaibles

# class Myclass:
#     name="john"  # Class variable
#
#     def __init__(self,name):
#         print(name) # David
#         print(self.name)  # John
#
# mc=Myclass("David")




#Example 8: A class with constructor and method

class Emp:

    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print(self.eid,self.ename, self.sal)


e1=Emp(101,"John",500000)
e1.display() #101 John 500000

e2=Emp(102,"David",600000)
e2.display()  #102 David 600000































