"""
Comparison Operators 
are used to compare values. 

They return a boolean value (True or False) 
based on the comparison.
"""

x = 5
y = 3
z = 5

# Equal to
print (x == y) # False, because 5 is not equal to 3

# Not equal to
print (x != y) # True, because 5 is not equal to 3

# Greater than
print (x > y) # True, because 5 is greater than 3

# Less than
print (x < y) # False, because 5 is not less than 3

# Greater than or equal to
print (x >= y) # True, because 5 is greater than or equal to 3

# Less than or equal to
print (x <= y) # False, because 5 is not less than or equal to 3



"""
Logical Operators
are used to combine conditional statements.

They include the following:
- and: Returns True if both statements are true
- or: Returns True if at least one statement is true
- not: Returns True if the statement is false
"""

print (x > y and y > z) # False, because while x > y is True, y > z is False
print (x > y or y > z) # True, because x > y is True

t = True
f = False
print(not t) # False, because t is True
print(not f) # True, because f is False