#
# mystring="welcome"
# print(len(mystring)) #7
#
# mylist=[10,20,30,40,50]
# print(len(mylist))  #5
#
#
# mytuple=(1,2,3,4,5)
# print(len(mytuple))
#
# mydic={"id":123, "name":"john"}
#
# print(len(mydic)) # 2



# Example for method overloading ( Polymorphism)

# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print("Hello "+ name)
#         else:
#             print("Hello")
#
#
# h=Human()
#
# #h.sayHello()
# h.sayHello("John")


#Example 2:

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)


cal=Calculation()

cal.add()  # 0
cal.add(10,20)  #30
cal.add(10,20,30)  # 60















