# Compiler and Interpreter:
# compiler: computer program that read program written in a high level language
# it can translate it into the same program
# in a low level language including machine language

# interperter: program that execute programming code directly
# coding style:

# x = 2 -> x stored 2
# python losely typed -> integer
# x = 'c' #: type -> string
# x = 2
# y = 'c'

# type class -> to know what is the type of this var
# print(type(x))
# print(type(y))

# assignments operators
# x = 2
# x = x + 2
# x += 2
# print(x)

# printing

# print("hello , ITI ")
# print('hello , ITI')

# print : function
# () : parentheses
# '' : single quotes
# "" : double quotes
# H E L L O : letter
# 'hello world' : string -> sequance of letter || character
#
# print("ITI")
# print("Python")
# comment # one line of comment

""" Doc String 
triple quotes multiple comments
nothing proceed here
"""

# print("AI")

# new line : \n string : add new line
# \ -> scape character -
# print("Hello \npython \nITI")
# print('hello',
#       'python',
#       'iti')

# Arithmatic Printing
# print(1+2+3)
# print('3'+'4')

# // -> integer division | division floor
# print                  (type(6//2))
#
# print(type(7/2))
# print(type('7/2'))

# Comma in printing
# , : is called comma -> doing space
# print("There is",1,"instractor not",2*3)
# _____________________________________________________

# Syntax Errors

# Don't forget
# print("Hello"
# " EOF" -> End of out file

# print('Hello")
# EOL

# print('Let's learn python')
# print('Let\'s learn Python') # using scape charachter
# print("Let's learn Python")
# print("Same for using \" in between")
# print('Same for using " in between')

# python is a case sensetive
# Print = 2
# print(type(Print))

# print(5)

# Indentation Error
# you have extra spaces
# x = "python"
#   y = "error"
# print(x , y)

# x = "python"
# y = "error"
# print(x , y)

# Python Data Types

# Numeric -> Integer, Float , Complex Number.
# Dictionary {Key,Value} -> Key,Value
# Boolean -> True, False
# Set -> () -> haven't duplicate
# Sequance Type -> String, List, Tuple

# Age = 23 -> integer
# Wegiht = 90.5 -> float
# Gender = Male || Femal -> boolean
# Name = "Mohame" -> string

# num = 1
# num = num *10 +2
# num = num *10 +3
# num = num *10 +4
# num = num *10 +5
# print(num)
# print(type(num))
# num = num / 10 +6
# print(num)
# print(type(num))

# Identifier (Var name)
# can't start with digit (5address)
# can't start with space or spechial char: < > / \ ? ! ( ) # $ % ^ & ~ + - *
# pythn case sensitive ->  sum!= SUM
# you shouldn't use reversed keyword (built in)
#
# print = 10
# print(print)

# SUM = 3
# sum = 4
# print("sum = ",(sum))
# print("SUM = ",(SUM))


# String

# print("Welcom in ITI")
# print("Welcom in" + " ITI") # concatinat string
# str1 = "Welcom in "
# str2 = "ITI "
# print(str1 + str2)
# print(str2*3) #ITI ITI ITI
# print(2 * str1 + str2)
# str3 = str1 + str2 + str1
# print(str3)

# \ escape char
# \t escape charachter for TAB
# default there is one every 8 spaces
# print("hello\tworld")
# print("hello\t\tworld")

# print("your age","is",27)

# min max function
# answer = min(3,6,7,1)
# print(answer)
#

# answer = min(4,7,-2)
# print(answer)
#
# answer = max(4,7,-2)
# print(answer)
#
# answer = max(9,6,4,7,-2,15,1)
# print(answer)

#  Length function len -> count
# str1 = "Python for machine Learning"
# print(len(str1))
# print(len(123)) #-> error

# print(len('7'))

# conversion | casting
# str_ = '10'
# str2 = "ITI"
# conv_str_to_int = int(str2)
# print(conv_str_to_int)
# print(type(str_))

# conv_str_to_int = int(str_)
# print(conv_str_to_int)
# print(type(conv_str_to_int))

# conv_str_to_float = float(str_)

# print(type(conv_str_to_float))

# conv_to_str = str(conv_str_to_int)
# print(type(conv_to_str))

# print(type(conv_str_to_int))

# print(len((conv_to_str)))

# Reading
# input function
# inp = input("Enter Your Name: ")
# print('your name is' , inp)

# inp = input("Enter any number: ")
# print(type(inp))
# 
# print("Hello " + input("Enter Your Name: "))

# a = input()
# b = input()

# print((a)+(b))
# print(type((a)+(b)))

# a = int(input())
# b = int(input())
# #
# print((a)+(b))
# print(type((a)+(b)))


# reading multiple input

# a,b,c = input().split()
# print(a,b,c)
# print(type(a))

# a,b,c = map(int, input().split())
# print(a,b,c)
# print(type(c))

# a,b,c = map(int, input("Enter Your number: ").split())
# print(a,b,c)
# print(type(c))

# Arithmatic Operators
# + - * / // %
# x = 3
# y = 6

# Binary operators , Unary operators
# Binary operators -> two operand
# print(x + y) # 9
# print(x + 2*y - 1) # 14 we called for it expression
#
# print(x/y)
# z = ((x + y) /3)/3
# print(z)
# print(12 % 5)

# print(65//50)
# print(type(99.5 //100))
# print(1500.0 // 99.0)

# print(1234//10)
# power operators
# x = 5**3
# print(x)
# print(2.1**4)

# Task
# num = 12345
# k = remove last k numbers
# k = 3
# res = 12
# num = 12345
# k = 2
# print(num // (10**k))

# Compound Assignment Opertors
# x = 1 + 2 * 5
# print(x)

# unary operator -> one operand
# ++x , --y , ++++z

# z = 4
# z += +z
# print(z)
# print(x)
# x-=4
"""
x -= 4
x = x - 4
"""
# print(x)
#
# x+=3
# print(x)
# x *= 2
# print(x)
# x //= 5
# print(x)
# x %= 6
# print(x)


# Multiple Assignments
# x,y = 5,7
# a, b, c = 'python', 12, 6.5
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))

# x = y = z = 1
# m = 3
# print(10 *m , m+1)
# print(x,y,z)
# x= 3
# print(x,y,z)
# print(10 - (6+3))
# str_1 , str_2, str_3 = "Hello" , "ITI" , "Python"
# print(str_1)
# print(str_2)
# print(str_3)
# print(str_1 , str_2, str_3)


# Boolean : True = 1 , False = 0
# print(bool(0)) #-> false
# print(bool('0'))# -> True

# status = True
# # print(status)
# # print(not status)
# print(bool('1')) 
# print(bool(''))
# print(bool(-5))
# print(bool(5.5))