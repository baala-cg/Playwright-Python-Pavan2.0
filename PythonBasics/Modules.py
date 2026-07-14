
######### Example 1: Importing functions and variables from a module

# File: operations.py

def add(num1, num2):
    print(num1 + num2)

def mul(num1, num2):
    print(num1 * num2)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


# File: client.py

# ---------------- Approach 1: Importing the whole module ----------------
import operations
operations.add(10, 20)   # Access using module name
operations.mul(10, 20)

# Access dictionary variable from module
a = operations.person1["age"]
print(a)


# ---------------- Approach 2: Importing specific functions ----------------
from operations import add, mul
add(10, 20)
mul(10, 20)


# ---------------- Approach 3: Importing everything (*) ----------------
from operations import *
add(10, 20)
mul(10, 20)




#########  Example 2: Handling same function names in different modules

# File: animal.py

def fly():
    print("Animal can't fly")

def color():
    print("Animal is Black")

# File: bird.py

def fly():
    print("Bird can fly")

def color():
    print("Bird is Green")


# File: animalbirdmain.py

# --- Approach 1: Importing with module names ---
import animal
import bird

animal.fly()     # Calls fly() from animal module
animal.color()   # Calls color() from animal module

bird.fly()       # Calls fly() from bird module
bird.color()     # Calls color() from bird module


# ---- Approach 2: Importing everything (*) -----
from animal import *
fly()    # Calls animal.fly()
color()  # Calls animal.color()

from bird import *
fly()    # Now fly() from bird overrides the previous one
color()  # Calls bird.color()

fly()    # Always refers to latest imported fly() i.e. bird.fly()




#########  Example 3: Using Classes from different modules
# File: a.py

class Animal:
    def display(self):
        print("I like Cow")


# File: b.py

class Bird:
    def display(self):
        print("I like Parrot")


# File: abmain.py

# ---- Approach 1: Importing full modules ------
import a
import b

obj1 = a.Animal()
obj1.display()   # Output: I like Cow

obj2 = b.Bird()
obj2.display()   # Output: I like Parrot


# ---- Approach 2: Importing specific classes ------
from a import Animal
from b import Bird

obj3 = Animal()
obj3.display()   # Output: I like Cow

obj4 = Bird()
obj4.display()   # Output: I like Parrot