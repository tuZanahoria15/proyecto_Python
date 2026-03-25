"""
Using Modules in Python:
In Python, a module is a file containing Python definitions and statements. 
It allows you to organize your code into separate files, making it easier to manage and reuse. 

You can create your own modules or use built-in modules provided by Python.
"""

# Importing the operations module
# import operations

# Using functions from the operations module
# print(operations.add(2, 5))        # Output: 7


"""
Another way to import specific functions from a module is by using the 'from' keyword.
This way allows you to save lines of code and directly use the functions, 
without prefixing them with the module name.

EXAMPLE:
from operations import add, substract, etc...
"""

from operations import add, subtract, multiply, divide

print(add(2, 5))        # Output: 7
print(subtract(10, 3))  # Output: 7
print(multiply(4, 6))  # Output: 24
print(divide(20, 4))    # Output: 5.0