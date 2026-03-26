"""
Try_Except:
It is a structure that allows us to handle exceptions in our code. 
It consists of a try block, where we write the code that may raise an exception, 
and an except block, where we handle the exception if it occurs.
"""

# Example of using try-except to handle a ZeroDivisionError
try:
    number = 10 / 2
    print("The result is:", number)
except ZeroDivisionError: 
    print("Error: You cannot divide by zero.")

print("______________________________/n")

# Declaring a variable 'x' to avoid NameError
x = 1

# Example of a variable IF is not defined, it will raise a NameError
try:
    print(x)
except NameError:
    print("Error: The variable 'x' is not defined.")



"""
Finally block:
Used to execute code that must run 
regardless of whether an exception occurred or not.
"""

try:
    print(x)
except NameError:
    print("Error: The variable 'x' is not defined.")
finally:
    print("This will always be executed.")