# Example 1:

class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0  # private variable

    # getter method
    def get_marks(self):
        return self.__marks

    #setter method
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks. Marks Must be <=100")

#usage
stu=Student("John")
stu.set_marks(90)
print(stu.get_marks())





