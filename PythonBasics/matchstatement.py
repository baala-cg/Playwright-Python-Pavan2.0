# The match statement is used to perform different actions based on different conditions.
# Instead of writing many if..else statements, you can use the match statement.

#Example 1:

# day=10
# match day:
#     case 1: print("sunday")
#     case 2: print("monday")
#     case 3: print("tuesday")
#     case 4: print("wednesday")
#     case 5: print("thursday")
#     case 6: print("friday")
#     case 7: print("saturday")
#     case _: print("Invalid week day")

# Example 2 : combine values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day =10
match day:
    case 2 | 3 | 4| 5| 6: print(" weekday")
    case 1 | 7: print("weekend")
    case _: print("invalid week")



















