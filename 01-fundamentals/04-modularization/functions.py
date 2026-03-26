"""
Functions for modularization:
A function is a block of code that performs a specific task. 
It can be reused multiple times in a program, which helps 
to reduce code duplication and improve readability. 

Functions can take input parameters and return output values, 
allowing for more flexible and modular code design.
"""

# Using def to define a function
def my_function():
    print("Hello, I am a function!")

# Calling the function
my_function()


print("________________\n")


# Custom function with parameters
# Important to set a default value for last_name, otherwise it will throw an error if we call the function without it
def greet(name, last_name=""): 
    print("Hello, ", name, last_name)

# The order and quantity of the parameters matters!!
greet("Fernando") # String parameter
greet("Fernando", "Sanabria") # String parameter with last_name

print("________________\n")

def greet2(name, nationality="Mexico"):
    print("Hello, ", name, "from", nationality)

greet2("Juan Carlos") # String parameter
greet2("Sergio", "USA") # String parameter with nationality


print("________________\n")


"""
Pass statement:
This is a placeholder for a function that does nothing, 
it can be used when we want to define a function but we don't have the implementation yet. 

It allows us to avoid syntax errors while we are still working on the function's logic.
"""
def regularFunction():
    pass  


"""
Basic Math functions:
# Functions can also return values, which can be used in other parts of the program.
In order to show the result of the function, we need to assign the return value to a variable.
"""
# Add
def add(a, b):
    return a + b

result = add(5, 3) # This will return 8
print("The result of adding 5 and 3 is: ", result)


# Subtract
def subtract(a, b):
    return a - b

result = subtract(10, 5) # This will return 5
print("The result of subtracting 5 from 10 is: ", subtract(10, 5)) # This will return 5


# Multiply
def multiply(a, b):
    return a * b

result = multiply(4, 6) # This will return 24
print("The result of multiplying 4 and 6 is: ", result) # This will return 24


# Divide
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

result = divide(10, 2) # This will return 5.0
print("The result of dividing 10 by 2 is: ", result) # This will return 5.0

result = divide(10, 0) # This will return an error message
print("The result of dividing 10 by 0 is: ", result) # This will return an error message