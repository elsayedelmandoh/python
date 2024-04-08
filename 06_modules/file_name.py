import sys
x= int(sys.argv[1]) # 'str' object cannot be interpreted as an integer, so convert it to a integer/
print([num for num in range(x) if num % 5 == 0])
