# # INPUT FUNCTION 
# # input() is a function that lets the user enter data into your program

# print() → output (computer → user)
# input() → input (user → computer)

name = input()
print(name)

# ///input() ALWAYS returns a string///

x = input()
print(type(name))

# You can’t add string + number
# so we need to do type conversion first before add input to integer

a = int(input())
print(a+19)

a = int(input("Enter the  value :"))
b = int(input("Enter the second value :"))
print(a+b)

# Multiple values in one line
a,b=input().split()
print(a,b)

# type conversion
a,b = map(int,input().split())
print (a* b)