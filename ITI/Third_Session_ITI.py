# data structure in python

# List , Tuple , Dictionary , set

# list - mutable, any kind of data or data type

# bracket []-> [0,1,2,3,..]
# seperate between item using comma ','

# lst = [1,2,3,4]
# print(len(lst)) # -> 4
#
# # check num in lst
# print(8 in lst) # condition -> True or false
#
# print list container
# for i in lst:
#     print(i, end = " ")
# print()
# print(lst)

# List can contain differnt data types
#  index of list start from 0
# lst = [1, "iti", 5.3]
# print(len(lst))
# lst[1] = 32
# print(lst)
# index out of range -> range(2)
# lst[3] = 0
# print(lst)


# build list from scratch
# create empty list
# lst = list()
# print(lst)
# i need to add 2 elem.
# append -> add
# lst.append("Book")
# lst.append(99)
# print(lst)
# lst.append('Cookies')
# print(lst)

# print(lst.pop())
# print(lst)
# print(lst[-2])

# 0   1  2  3  4 -> index of value
# 5   3  4  8  9 -> value
#-5  -4 -3 -2 -1 -> negative index

# lst = [5,3,4,8,9]
# print(lst[-3])

#
# Mutable
# lst = [1,2,3,4,5]
# lst[0] = 9
# print(lst)

# indexing
    # 9    2  21 5  4 
# num = [10 ,2, 7, 5, 3]
# num[0] = 9
# num[2] *=3
# num[4] +=1
# print(num[4])
# print(num)

# for idx in range(5): # 0 -> 4
#     print(num[idx] , end= ' ')

# index -> 0 1 2 3 4

# numbe -> 9 2 21 5 4

#  + and * operators

# lst = [1, 'ITI' , 5]
# another_list = [99, 11.5]
# # # concatination lists
# conc_lst = lst + another_list
# # print(conc_lst)
# # #
# thrd_lst = 3 * conc_lst
# print(thrd_lst)

# Append , extend and insert
# lst = [1,2,3,4,5]
# lst.append('Hello')
# # print(lst)
# # #
# another_lst = [3,1]
# another_lst.extend(lst)
# print(another_lst)

#insert take position and value
# lst.insert(2 , "wow")
# print(type(lst)) # -> list
# for i in lst:
#     print(i ,type(i))
# print()

# Pop , remove , del
#
# lst = [1,5,10,17, 2,"ITI"]
# print(lst.pop())
# print(lst)
# # take index
# print(lst.pop(3))
# print(lst)

# # remove take value
# lst.remove(5)
# print(lst)

# del take index
# print(del lst[0]) # Error
# print(lst)

# clear
# print(lst)
# lst.clear()
# print(lst)

# lst = [1,2,3]
# print(id(lst))
# ________________________________________

# function
# block -> of code
# print("Hello")
# print("ITI")
# print("Python")


# def Printing():
#     print("Hello")
#     print("ITI")
#     print("Python")

# Printing()
# Printing()

#def-> define function
# def funName(parameter)
# def nums_op(fNum , sNum):
    # print("Sum: ",fNum + sNum)
    # print("Multiplication: ",fNum * sNum)
#
# nums_op(arguments)
# nums_op(5,6)


"""
1 2 3 5 10 12 15 18 27 100 -> increase
1 2 3 5 10 6 12 15 -> not increasing 
"""



# slicing in list
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(type(lst))

# print(type(range(5)))

# slice_lst = lst[2:8]
# print(slice_lst)

# sl_lst = lst[2:] # from index 2 to end
# sl_lst = lst[2:100000]
# print(sl_lst)
# sl_lst = lst[:5]
# print(sl_lst)
# sam_val = lst[:4] + lst[4:6]
# print(sam_val)
# print(lst[:])

# slice with steps
# slicing list[start:end:stpes]
# lst = [1,2,3,4,5,6,7,8,9,10]
# sub_lst = lst[: :-2]
# print(sub_lst)

# list comperehinsion
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = []
# for i in lst1:
#     lst2.append(i*i+1)
# print(lst2)

# list comperehinsion
# lst2 = [expression for increment in lst]

# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = [i*i+1 for i in lst1]
# print(lst2)

# lst = [1,2,-4,3,-3,-7,6,-1]
# print(min(lst))
# print(max(lst))
# print(sorted(lst))
# print(lst)

# lst2 = []
# for i in lst:
#     if i > 0:
#         lst2.append(i)
# print(lst2)
#
# lst3 = [i for i in lst if i>0]
# print(lst3)


# Tuples
# another an order collections of objects
# similer list
# iter , indexing, slicing, comparason, func -> min, max, sorted()

# more
"""
immutable data type: we can't change or delete iths item
many methods -> append , insert , remove
"""
# tu = tuple()
# tup = (5,6,7)
# x,y,z = tup
# print(x,y,z)

"""
swap in one line
"""
# x,y = y,x
# print(x,y,z)

# x = 5
# y = 6
# x = x*y = 30
# y = x / y = 5
# x = x / y  = 6


# lst =[1,2,3, [4,5,6,[7,8,9]], [10,11,12]]

# creation
# tup = ("iti" , 12, 3.4 , [1,2,3])
# print(tup)
# print(len(tup))
# print(type(tup))

# t = (10)
# print(t)
# print(type(t))
#
# t = (10,)
# print(type(t))

# t = tuple('ITI')
# print(t)
# print(type(t))
#
# t = tuple((1,2,3))
# print(type(t))
# print(t)
#
# t = tuple([1,2,3])
# print(len(t))
# print(type(t))

# indixing and slicing
# num = (1,2,3,6,4,5,3,1,6,1,3,3,6)
# print(num[0] , num[5])
# print(num[1:4])
# print(num[::])
# methods and function
# print(num.count(3))

# print(num.index(6)) #-> index of value

# print(min(num),max(num))
# print(sorted(num))

# reversed
# num = (1,2,3,4,5,6)
# print(tuple(reversed(num))) # -> 6,5,4,3,2,1

# t1 = tuple(([1],[2],[3]))
# print(len(t1))

#  + and * operators
# t1 = (1,2,3)
# print(type(t1))
# t2 = ("ITI", True)
# #

# t = t1+ 2*t2
# print(t)
# print("hi "*2)


# Unpacking
lst = 1,2,3,4,5
# a,b,*c = lst
# print(type(a))
# print(b)
# print(type(c))

# a,b,*c = lst
# print(a)
# print(b)
# print(c)

# *a,b,c = lst
# print(a)
# print(b)
# print(c)

# a,*b,c = lst
# print(a)
# print(b)
# print(c)

"""
num = 1,2,3,4,5
a,b,c = num

unpacking
a,b, *c = num

a, *b ,c = num

*a , b,c = num
"""

# lst1 = [1,2,3]
# lst2 = [4,5,6]
# conc = [*lst1 , *lst2]
# print(conc)

"""
Dictionary and Set
dictionary like list but it have key, value
key -> immutable
value -> mutable
"""

# lst = [1,2,33]
# print(lst[1]) # -> index

# x = {k:v}
# dictionary = {Key : Value}
# dic = { 0:1 ,
#         1:2 ,
#         213: 3}
# print(dic[213])
# print(dic[0])

# dic = {
#     'p' : 'Python',
#     'i' : "ITI",
#     's' : "Summer"
# }
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic['p'])

# update and delete
# dic = {}

# key       #value
# dic[12] = [234,(1,"ITI")]
# print(dic)
# dic["ITI"] = 20

# print(dic.keys())
# print(dic.values())
# print(dic)

# del func
# del dic[12]
# print(dic)
# print(type(dic))

# ____________________________________

# Indinxing dic values
# dic = {
#     "ITI" : "Learn",
#     1 : [1,5,7,8],
#     3: [[3,4],[8,9,10]]
# }

# print(dic["ITI"])
# print(dic["ITI"][-1])
# print(dic[1][1])
# print(dic[3][0][1])

dic = {
    int : [1,2,3],
    2: 40,
    2: 50
}
"""
key    value
2   ->  50
"""
# print(dic[2])
# # # get method
# dic[]
# print(dic.get(2))
# print(dic.get(int))

# dic = {'x':11 , 'b':22 , 'y': 30}
# dic['a'] = 33
# print(dic)
#
# while dic:
#     print(dic.popitem())

# clear -> dic.clear() -> remove all keys
# print(dic)
# print(dic.clear())
# print(dic)

# set -> () -> not repeated any values and sorted this values
# lst = [1,2,1,4,2,6,4,5,1,8,2,8,9,8,4,9,"ITI"]
# st = set(lst)
# print(st)


#function 
# Define Function

"""

1- somthing is written and ready to use
2- we write once, and start using at any time
3- it saves everyone time
4- python provide built in function

"""

# Parameter vs. argument
"""
1- Parameter: the var used in defineing the function
2- Argument: is an expression passed to the function
"""

# return keyword
# return some result from our function
# def our_min(fNum, sNum):
#     if fNum < sNum:
#         return (fNum)
#     else:
#         return (sNum)
# print(our_min(5,6))

# def our_max(fNum, sNum):
#     if fNum > sNum:
#         return fNum
#     else:
#         return sNum

# a,b = 10,20

# print("Maximum number:" , our_max(9,100))
# print("Minimum number:" , our_min(9,100))

# OOP
# Class

# class Employee:
#     name = None
#     salary = None
#     address = None

# Emp = Employee()
# Emp.name = "Mohamed"
# Emp.salary = 1000
# Emp.address = "Egypt"
# print(Emp.address)

# Emp2 = Employee()
# Emp2.name = "Ahmed"
# Emp2.salary = 2000
# Emp2.address = "Cairo"
# print(Emp2.salary)

# Constractor
# class Employee:
#     def __init__(self,name):
#         self.nm = name

# obj1 = Employee("Mohamed")
# print(obj1.nm)

# class Employee:
#     name = None
#     salary = None
#     address = None

# def print_emp(obj):
#     print("Emp name:", obj.name)
#     print("Emp salary:", obj.salary)
#     print("Emp address:", obj.address)

# emp = Employee()
# emp.name = "Ahmed"
# emp.salary = 5000
# emp.address = "Giza"

# print_emp(emp)


# class Employee:
#     name = None
#     salary = None
#     address = None

# def print_emp(obj):
#     print("Emp name:", obj.name)
#     print("Emp salary:", obj.salary)
#     print("Emp address:", obj.address)

# def read_emp():
#     obj = Employee()
#     obj.name = input("Enter Employee name: ")
#     obj.salary = input("Enter Employee Salary: ")
#     obj.address = input("Enter Emp Address: ")
#     return obj

# emp = read_emp()
# print_emp(emp)

# Methods

# methods are functions
# define inside the body of a class
# the first parameter is referring to the object itself

# using . operator call the methods
# class Employee:
#     name = None
#     salary = None
#     address = None

#     def print_emp(self):
#         print("Emp name:", self.name)
#         print("Emp salary:", self.salary)
#         print("Emp address:", self.address)

#     def read_emp(self):
#         self.name = input("Enter Employee name: ")
#         self.salary = input("Enter Employee Salary: ")
#         self.address = input("Enter Emp Address: ")
        

# emp = Employee()
# emp.read_emp()
# emp.print_emp()