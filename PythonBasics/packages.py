####### Example 1: Importing modules from a single package

'''
pack1/
 ├── module1.py
 └── module2.py
'''

# File: module1.py

def display():
    print("This is display function from module1")

# File: module2.py

def show():
    print("This is show function from module2")


# File: client.py

import sys
sys.path.append("C:/Automation/PWPython/day13/pack1") # Add package path to system path

# ------ Approach 1: Importing full modules -----
import module1
import module2

module1.display()   # Calls display() from module1
module2.show()      # Calls show() from module2


# ------ Approach 2: Importing everything (*) ------
from module1 import *
from module2 import *

display()   # Directly calls display() without module name
show()      # Directly calls show()
show()      # Can be called multiple times




###########  Example 2: Importing modules from different packages

'''
pack1/
 ├── module1.py
 └── pack2/
     └── module2.py
'''


# File: module1.py
def display():
    print("This is display function from module1")

# File: module2.py
def show():
    print("This is show function from module2 inside pack2")


# File: client.py

import sys
sys.path.append("C:/Automation/PWPython/day13/pack1") # Add pack1 path and import module1
from module1 import *

sys.path.append("C:/Automation/PWPython/day13/pack1/pack2") # Add pack2 path and import module2
from module2 import *

display()   # Calls module1.display()
show()      # Calls module2.show()





########  Example 3: Importing classes from different modules & packages
'''
pack1/
 └── emp.py      (Employee class)

pack2/
 └── stu.py      (Student class)

pack3/
 └── client.py   (Imports both classes and uses them)

'''

# File: emp.py

class Employee:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def displayemp(self):
        print("empid:{} empname:{} empsal:{}".format(self.eid, self.ename, self.sal))


# File: stu.py

class Student:
    def __init__(self, sid, sname, sgrad):
        self.sid = sid
        self.sname = sname
        self.sgrad = sgrad

    def displaystu(self):
        print("stuid:{} stuname:{} stusal:{}".format(self.sid, self.sname, self.sgrad))


# File: client.py

import sys

# Import Employee from pack1
sys.path.append("C:/Automation/PWPython/day13/pack1") 
from emp import Employee
e = Employee(101, 'Scott', 40000)
e.displayemp()   # Output: empid:101 empname:Scott empsal:40000


# Import Student from pack2
sys.path.append("C:/Automation/PWPython/day13/pack2")
from stu import Student

s = Student(141, 'David', 'A')
s.displaystu()   # Output: stuid:141 stuname:David stusal:A

