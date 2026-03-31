# # A variable is a name given to a value stored in memory
# Computer memory = storage
# Variable = label on that storage

# Python automatically detects type:
x = 10        # int
y = 3.14      # float
z = "hello"   # string
a = True      # boolean

print(type(y))
# type(__) gives which data type is that variable

# You CANNOT use Python keywords:
# if = 10   ❌
# for = 5   ❌

# multiple assessment
a, b, c, name = 1, 2, 3, "bhuvvv"

print(a, b)

x = y = z = 0
print(x)
print(y)

# Swapping Variables
a = 100
b = 200

a, b = b, a

print(a)

# Type Conversion
x = "10"
y = int(x)
print(y+5)

# float(10)
# str(100)
# bool(1)

# Memory Concept
# x = 10
# y = x
# What you THINK:
# x has 10
# y has 10
# What ACTUALLY happens:

#  Python creates one object: 10 in memory

#  Then:

# x points to that object
# y ALSO points to that same object

# Now change x
# Python does NOT change 10 into 20
#  Instead:

# Creates a NEW object 20
# Makes x point to it
