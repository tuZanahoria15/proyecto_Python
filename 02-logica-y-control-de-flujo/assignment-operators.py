"""
Assignment Operators 
are used to assign values to variables. 

They include the basic assignment operator (=) 
as well as compound assignment operators that combine 
an arithmetic operation with assignment.
"""

x = 5

# Addition assignment
x += 3  # This is equivalent to x = x + 3

# Subtraction assignment
x -= 3 # This is equivalent to x = x - 3

# Multiplication assignment
x *= 3 # This is equivalent to x = x * 3

# Division assignment
x /= 3 # This is equivalent to x = x / 3

# Modulus assignment
x %= 3 # This is equivalent to x = x % 3

print ("Current value of x: ", x)



y = 20

# Floor division assignment
y //= 2 # This is equivalent to y = y // 2

# Exponentiation assignment
y **= 2 # This is equivalent to y = y ** 2

print ("Current value of y: ", y)



"""
Walrus operator (added in Python 3.8)
The walrus operator (:=) allows you to assign a value 
to a variable as part of an expression.

It is useful for situations where you want to use 
the value of a variable immediately after assigning it, 
without needing to write a separate assignment statement.
"""

print (z := 3)
print (z) # z is now assigned the value 3, and we can use it later in the code

