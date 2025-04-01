
# Basic Syntax of Python
print("Hello World")

# Comments in Python

# This is a single line comment

"""This
   is a
   multiline 
   string"""

# Python Variables

# what is variables?
# Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.

# In python we do not need to declare variable type just need to assign value to the variable 

name = 'Urooj'  #String
age = 20        #int
height = 5.0    #float
student = True  #boolean


"""Scope of Variable
     The scope of the variable is the area within which the variable has been created. 

 there are two types of variable

1: Local Variable:
    A local variable is created within a function and can be only used inside that function. 

2: Gloabal Variable
    A  global variable is created in the main body of the code and can be used anywhere within the code. 
"""

fruit = 'Apple'    #global variable

def food():
    vegetable = 'Potato'  #local variable  
   
    print(vegetable + ' is a local variable ')

food()

# print(vegetable + ' is a local variable ') #so it will give error as it is a local varibale can not call out of the scope
print(fruit + ' is a gloabal variable ')
