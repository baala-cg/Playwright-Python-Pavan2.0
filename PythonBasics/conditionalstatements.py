# if

#Example 1 : age>=18  eligible
# age=15
# if age>=18:
#     print("eligible for vote")

#Example 2: Check the amount value after discount

# amount=500
# discount=0
#
# if amount>1000:
#     discount=amount*10/100
#
# print("Actual amount after reducing discount:", amount-discount)


# if else condition

#Example 1:  check person eligibility & ineligibility for vote

# age=15
#
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


#Example 2: check the number is even or odd

# num=11
#
# if num%2==0:
#     print(num,   "Even number")
# else:
#     print(num, "Odd number")



# if elif else

#Example 1:
# Suppose there are different slabs of discount on a purchase −
# 20% on amount exceeding 10000,
# 10% for amount between 5000-10000,
# 5% if it is between 1000-5000
# no discount if amount<1000

# amount= 500
# print("Actual amount: ", amount)
#
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount=amount*10/100
# elif amount>1000:
#     discount=amount*5/100
# else:
#     discount=0
#
# print("Payment amount after discount:", amount-discount)


#Example2: 1-sunday   2-monday
#
# weekno=10
#
# if weekno==1:
#     print("sunday")
# elif weekno==2:
#     print("monday")
# elif weekno==3:
#     print("Tuesday")
# elif weekno==4:
#     print("Wednessday")
# elif weekno==5:
#     print("Thursday")
# elif weekno==6:
#     print("Friday")
# elif weekno==7:
#     print("saturday")
# else:
#     print("invalid week number")





###   Nested if else statements


# num ---> 2 , 3
# num ---> 2   but 3
# num ---> 3 but 2
# num---> not 2 not 3

# num=6
# print("Number:", num)
#
# if num%2==0:
#     if num%3==0:
#         print("divisible by both 2 & 3")
#     else:
#         print("divisible by 2 but not 3")
# else:
#     if num%3==0:
#         print("divisible by 3 but not 2")
#     else:
#         print("not divisible by 2 and 3")



## Short hand if
# a,b=20,10
#
# if a>b:
#     print("a is greater")
#
# if a>b:print("a is greater")


## Short hand if else  ( ternary operator)
# a,b=20,10
#
# if a>b:
#     print("a is greater")
# else:
#     print(" b is greater")
#
#
# print("a is greater") if a>b else print("b is greater")    # ternary operator




# And ( logical operator) with if elif else
# find largest of 3 numbers
# a, b, c
#  a>b and a>c   a is largest
#   b>a and b>c  b is largest
#  c is largest

# a=30
# b=200
# c=50
#
# if a>b and a>c:
#     print(" a is largest ", a)
# elif b>a and b>c:
#     print(" b is largest", b)
# else:
#     print(" c is largest", c)




# pass
a=10
b=100

if a>b:
    pass

print("something")
































