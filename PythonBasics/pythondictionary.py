# Dictionaries are used to store data values in key:value pairs.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionary items are ordered, changeable(mutable), and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#  { }

# 1. creating a dictionary

#Approach 1:
#mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic={
#         "brand" : "Ford",
#         "model": "Aspire",
#         "year" : 2024
#     }
#
# print(mydic)  #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}


#Appraoch 2: using dict() constructor
# mydic=dict(name="John", age=35, country="India")
# print(mydic)  # {'name': 'John', 'age': 35, 'country': 'India'}


#a key can have multiple values
# mydic={
#     "brand" : "Ford",
#     "model": "Aspire",
#     "year" : 2024,
#     "colors":["red","white","blue"],
#     #"brand" : "Hyundai"
#  }
# print(mydic) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024, 'colors': ['red', 'white', 'blue']}



# 2. Accessing items from dictionary

#You can access the items of a dictionary by referring to its key name, inside [] brackets:

#Appraoch 1:
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(mydic["model"]) #Aspire

# Appraoch 2: using get() method
# print(mydic.get("brand")) #Ford


# 3. Get Keys : keys() method will return a list of all the keys in the dictionary.

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(mydic.keys()) #dict_keys(['brand', 'model', 'year'])

# 4. Get Values:  values() method will return a list of all the values in the dictionary.

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(mydic.values()) #dict_values(['Ford', 'Aspire', 2024])


# 5. Get Items : items() method will return each item in a dictionary, as tuples in a list.

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(mydic.items())
# print(mydic)



# 6 .  Check if key is exists ( searching key in a dictionary)

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
#
# if "model" in mydic:
#     print("Exists")
# else:
#     print("not exists")


# 7. Adding items to the dictionary
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic["color"]="red"
# print(mydic)  #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024, 'color': 'red'}



# # 8. updating dictionary  - update()
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic["color"]="red"
# print("Before updating:", mydic) #'brand': 'Ford', 'model': 'Aspire', 'year': 2024, 'color': 'red'}
#
# mydic.update({"year":2025})
# mydic.update({"color":"white"})
# print("After updation:", mydic) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2025, 'color': 'white'}



#9. removing items from dictionary

#Appraoch 1: using pop()
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic.pop("model")
# print(mydic) #{'brand': 'Ford', 'year': 2024}


#Approach 2 : using popitem()
#removes the last inserted item (in versions before 3.7, a random item is removed )
#
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic.popitem()
# print(mydic) #{'brand': 'Ford', 'model': 'Aspire'}


#Appraoch 3: using del keyword - removes the item with the specified key name

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# del mydic["model"]  # this will remove only model item
# print(mydic) #{'brand': 'Ford', 'year': 2024}
#
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# del mydic   # delete dictionary completly
# print(mydic) #NameError:


#Appraoch 4: The clear() method clears the dictionary

# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic.clear()
# print(mydic)  #{}


# 10. Copying the dictionary
#Appraoch 1: using copy()
# mydic1={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic2=mydic1.copy()
#
# print(mydic1) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}

# Appraoch 2: using dict()

# mydic1={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# mydic2=dict(mydic1)
# print(mydic1) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2) #{'brand': 'Ford', 'model': 'Aspire', 'year': 2024}


#11. length of dictionary
# mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }
# print(len(mydic))  #3


# 11. looping with dictionary

mydic={ "brand":"Ford", "model":"Aspire", "year" : 2024 }


#Print all key names in the dictionary, one by one
# for x in mydic:
#     print(x)
#
# for x in mydic.keys():
#     print(x)

#Print all values in the dictionary, one by one

# for x in mydic:
#     print(mydic[x])

# for x in mydic.values():
#     print(x)


# Print all the items from teh dictionary
for x,y in mydic.items():
    print(x,y)



