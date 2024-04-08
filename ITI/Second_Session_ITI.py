# comparing strings
# print("letters" < "letter") # False
# print("char" < "letter") # true
# print("char" != "char") # False
# print("char" != "cher") # true
# print("A" != "a") # True

# Logical Operators

# age , salary = 30 , 7000
# result = (age > 25) and (salary < 8000)
# print(result)

# print(age > 25 and salary > 9000)
# print(age > 35 or salary < 8000)
# print(age > 35 and salary > 9000)

# mixing logical operators
# age , salary  , weight = 30 , 7000 , 110
#
# #  True or False
# print(age > 25 and salary < 8000 and weight < 1500)
# print(age > 25 and salary < 8000 and weight > 200)
# print(age > 35 and salary > 6000 or weight > 200)

# status = weight >= 150
# print(status)

# print(age > 25 and salary < 8000 and not status)
#
# print(2 > 10 or 6 > 2)
# x = 4
# y = 5
# print(x,y)
"""
Conditions
1st style
if condition:
    body -> single line or multi line or complex logic or more if's
    "Identation"
    

2nd style 
if condition:
    body
elif condition:
    body
elif condition:
    body
elif condition:
    body
    
    
3rd style
if condition:
    body
elif condition:
    body
elif condition:
    body
elif condition:
    body
else:
    body
"""

# x = 5
#
# if x < 10:
#     print("smaller")
# #
# if x > 20:
#     print("Bigger")
#
# print("finish program")

# comparing operators
# x = 5
# if x == 5:
#     print("Equal 5")
# if x > 4:
#     print("Greater than 4")
# if x >= 5:
#     print("Greater than or equal 5")
# if x < 6:
#     print("Less than 6")
# if x <= 5:
#     print("Less than or equal 5")
# if x != 6:
#     print("Not equal 6")

    # """"
    # Equal 5
    # Greater than 4
    # Greater than or equal 5
    # Less than 6
    # Less than or equal 5
    # Not equal 6
    # """
# x = 5
# print("Before 5")
# #
# if x == 5:
#     print("Is 5")
#     print("Is still 5")
#     print("Third 5")

# #
# print("After 5")
# print("Before 6")
# #
# if x == 6:
#     print("Is 6")
#     print("Is still 6")
#     print("Third 6")

# print("After 6")

# nested if condition
# num = int(input("Enter Number: "))

# if 100 <= num <= 200:
#     print("Let's go")

#     if num % 2 == 0:
#         print("even number")

#         if num == 150:
#             print("150 is lucky number")
#         else:
#             print('Not 150')
#     else:
#         print("Bye Mr odd")
# else:
#     print("Have a good day")


# # Simple Calculator
# num1, op, num2 = input("Enter your number and operator: ").split()
# num1,num2 = float(num1),float(num2)
# #
# if op == '+':
#     print(num1+num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == "*":
#     print(num1*num2)
# else:
#     if num2 > 0:
#         print(num1/num2)
#     else:
#         print("N/A")

# Minimum 0f 3 numbers

# x,y = input().split()
# x,y = map(float, input().split())

# num1 , num2 , num3 = map(int, input("Enter yor numbers: ").split())
# #
# if num1 < num2:
#     if num1 < num3:
#         # print("Num_1: ",num1,"Is minimum")
#         print(num1)
# else:
#     if num2 < num3:
#         # print("Num_2: ",num2,"Is minimum")
#         print(num2)
#     else:
#         # print("Num_3: ",num3,"Is minimum")
#         print(num3)
#
# if num1 < num2 and num1 < num3:
#     print("Num_1: ", num1, "Is minimum")
# elif num2 <= num1 and num2 <= num3:
#     print("Num_2: ", num2, "Is minimum")
# else:
#     print("Num_3: ", num3, "Is minimum")

# ans = num1
# if ans > num2:
#     ans = num2
# if ans > num3:
#     ans = num3
# print(ans)

# Loops

# while loop

# initialization
# condition
# action
# increment step
# we call every step on iteration

x = 1 # -> initialization
# while x <= 5: # -> condition
#     print(x, end= " ") # -> action
#     # print(x)
#     x = x+1 # -> increment step

# print(x)

# x = 6
# while 2 < 5 and x >= 0:
#     print("Hello")
#     x -= 1

# sum 1+2+3+4+5
# x = 1
# sum_1 = 0
# while x <= 5:
#     sum_1+=x
#     x = x+1
# #     x+=1
# print(sum_1)
# print(x)

# break -> tell computer stop this condition
# reading 2 numbers and print thier float division if 2nd number zero -> print "Bye" and End the program

# while True:
#     x,y = map(float, input("Enter 2 Number: ").split())
#     if y == 0:
#         print("Y is ZERO")
#         break
#     print(x/y)
# print("bye")

# continue -> tell computer jump to the while start again continue from there
# while True:
#     x,y = map(float, input("Enter 2 Number: ").split())
#     if y == 0:
#         print("Y is ZERO")
#         continue   # jump to wile loop line
#     print(x/y)
#     break
# print("bye")

# numbers divisible by 3
# read an integer number then print all numbers that are divisible by 3 from 1 to x
# 10 -> 3 , 6 , 9

# num = int(input("Enter Your number: "))
# start = 1
# while start < num:
#     if start % 3 == 0:
#         print(start, end=" ")
#     start += 1
# print()
# print(start)

# Return Length of number digits

# int 11 -> len(not int) , casting from int to string , len( casting )

# num = int(input("Enter number: "))
# digit = 0
# # num = 1001
# # num = 89651
# # num = 0001
# while num > 0:
#     # digit += 1
#     digit = digit + 1
#     # num //= 10
#     num = num // 10 # 0001 // 10 -> 000 1
# print(digit)
# pos = 0
# while pos < 5:
#     print(pos, end = ' ')
#     pos+=1
# else:
#     print()
#     print("Hello")
#     print(pos)

# for loops
# the range function return
# sequance of number:
# start from default 0
# increment default by 1
# stops before a specified number.

# for loop syntax
# for i in range(5):
#     print(i)

# i =0
# while i<5:
#     print(i)
#     i+=1
    # i = i+1

# range (start, end, increment)
# start default = 0
# increment default = 1

# for i in range(2,5):
#     print(i , end=" ")


# for i in range(1,21,4):
#     print(i, end =" ")

# rng = range(1,21,4)
# for i in rng:
#     print(i, end =" ")

# iteration backword
# for i in range(5,0,-1):
#     print(i)


# for i in range(5):
#     pass

# for i in range(5):
#     ...

# for with string
# string -> sequence of character
# mystr = "Python"
# for char in mystr:
#     print(char,end =" ")

# enumerate
# get index of position

# mystr = "Python"
# for i , j in enumerate(mystr):
#     print(i,j)

# for i in enumerate(range(5,10)):
#     idx,val = i
#     print(idx,val)

# nested for loop
# tc = int(input("Enter Test Cases: "))
# for cases in range(tc):
#     n , sum_ = int(input("Enter Number: ")) , 0
#     for pos in range(1,n+1):
#         sum_+=pos
#     print("Sum from 1 to ",n, sum_)

# nested for loop program to print multiplication table
# for i in range(1,11):
#     for j in range(1, 11):
#         print(i*j , end = ' ')
#     print()

# for i in range(5):
#     print(i, end = " ")
# else:
#     print("\nNo items left")

# for i in range(6):
#     print(i)
# print(i)
# if i==5:
#     print("No item left")
# else:
#     print("We stop at 4")