print("Hello World")

# BAsic syntax : print(value1,value2,..., sep="", end="\n")
print("Hello") #string 
print(10)# interger 
print(3.14)#decimal /float
print(True)#boolean 

# multiple variable
print ("hello","world")

# Seperator inside print()
print("hello", "world",sep="-")

print(1,2,3,4 , sep= " ^")

print("2023","06","12" , sep= "/")

# End Line ending in python 
print("hello","world ", end= "\n")

print("hello ", end=" ")
print("world")

print("hello ", end="..... " )
print("world")

print("hello \nworld")

# Escape characters
# \n → new line
# \t → tab space
# \" → double quote
# \\ → backslash

print("hello \" world")
print("Hello \\ world")
print("Hello \t world")

# String Concatenation vs Comma
print("Hello" + "World")
print("Hello", "World")

# +  joins without space
# ,  adds space automatically


# printing variables 
name = "bhuvann"
age = 20
print("Name:",name,"Age:",age)
print(f"the name is {name}, Age is {age} years.")

# where (f"....") it add the function inside the "" itself it makes the coding easy 

# Formation the numbers in print()
price = 98.5467347564346
print(f"  the price of the product is {price:.4f}")
print(f"  the price of the product is {price:.8f}")
print(f"  the price of the product is {price:.2f}")
# here .__f give how many decimal numbers...

# Practice Tasks
name= "Bhuvan "
age = 20
print(f"Name : {name} | Age : {age}")

print("2026","03","30", sep="-")

print("Hello", "World", end="\n")

print(f"The total is {price}")