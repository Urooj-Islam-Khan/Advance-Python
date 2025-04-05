# Task 1: Basic Operations
# 1: Create a variable x with the value 10 and y with the value 20.

x = 10 
y = 20

# 2: Perform the following operations:

# Add x and y.
print(x+y)
# Subtract y from x.
print(x-y)
# Multiply x and y.
print(x*y)
# Divide y by x.
print(y/x)
# Find the remainder when y is divided by x.
print(y%x)
# Find the result of x raised to the power of y.
print(x**y)
# Find the floor division of y by x.
print(y//x)

# Task 2: Data Types
# 1: Create variables for each of these data types: int, float, str, bool, and list.

int_var = 25
float_var = 3.14
str_var = "Urooj"
bool_var = True
list_var = (1,2,3,4,5)

# Task 3: Comparison Operators
# Create two variables a = 25 and b = 10.
a = 24
b = 10
# Compare a and b using the comparison operators (==, !=, >, <, >=, <=). Print the result of each comparison.

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# Task 4: Logical Operators
# Create two Boolean variables x = True and y = False.
x= True
y= False
# Use and, or, and not operators to combine them and print the results.

print(x and y)
print(x or y)
print(not x, not y)

# Task 5: String Operations
# Create a string variable name = "Alice".
name = "Alice"
# Concatenate name with another string " is learning Python", and print the result.

name2 = name + " is learning Python"
print(name2)

# Use string slicing to get the first three characters of the string.
print(name[:3])

# Task 6: Floor Division & Exponentiation
# Create two variables m = 8 and n = 3.
m = 8
n= 3
# Perform floor division m // n and exponentiation m ** n.
# Print the results of both.
print(m//n)
print(m**n)

# Task 7: Type Conversion
# Convert an integer to a float and a float to an integer, then print both results.
a = 12
b = 3.14
print("before conversion")
print(type(a), type(b))
print("after conversion")
c = float(a)
d = int(b)

print("after conversion")
print(type(c), type(d))

# Convert a string "100" to an integer and perform a mathematical operation.

str = "100"
str = int(str)
print(25 + str)

# Task 8: List and Operators
# Create a list my_list = [1, 2, 3, 4].

my_list =[1,2,3,4]
# Add an element to the list.

my_list.append(5)
# Check if an element exists in the list using the in operator.
print(2 in my_list)

# Task 9: Assigning Multiple Variables
# Use a single line of code to assign values to a, b, and c (e.g., a = 1, b = 2, c = 3).
a,b,c =1,2,3
# Print the values of a, b, and c.
print(a,b,c)