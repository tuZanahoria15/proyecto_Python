"""
Lambda:
Is an anonymous function, it can have any number of arguments 
but only one expression, which is evaluated and returned.
"""

# Regular examples
x = lambda a : a + 10 # Set an argument a, and return a + 10
print(x(5)) # This will return 15, because 5 + 10 = 15

y = lambda a, b : a + b # Set two arguments a and b, and return their sum
print(y(2, 3)) # This will return 5, because 2 + 3 = 5



# Practical example of using lambda functions:
def my_function(n):
    return lambda a : a * n # This will return a function that multiplies its argument by n

duplicate = my_function(2) # This will create a function that multiplies its argument by 2
triple = my_function(3) # This will create a function that multiplies its argument by 3

print (duplicate(5)) # This will return 10, because 5 * 2 = 10
print (triple(5)) # This will return 15, because 5 * 3 = 15

print("________________\n")

cuadruple = my_function(4) # This will create a function that multiplies its argument by 4
quintuple = my_function(5) # This will create a function that multiplies its argument by 5

print (cuadruple(5)) # This will return 20, because 5 * 4 = 20
print (quintuple(5)) # This will return 25, because 5 * 5 = 25

