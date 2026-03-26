x = 1 # Integer
y = 2.5 # Float
z = 1j # Complex number

# Use of Type() function to check the data type of the variables
print(type(x)) #Which is <class 'int'>
print(type(y)) #Which is <class 'float'>
print(type(z)) #Which is <class 'complex'>

possitiveNumber = 5.5
negativeNumber = -3.2

imaginaryNumber = -5 -1j



""" 
Casting is the process of converting 
a variable from one data type to another.
"""
xf = float(x) #Converts the integer x to a float
print (xf) #Prints 1.0

ye = int(y) #Converts the float y to an integer
print (ye) #Prints 2



""" 
Usage of Complex numbers
"""
integer = 5
float = 3.14

integerComplex = complex(integer)
floatComplex = complex(float)

print(integerComplex) #Prints (5+0j)
print(type(integerComplex)) #Prints <class 'complex'>
print(floatComplex) #Prints (3.14+0j)
print(type(floatComplex)) #Prints <class 'complex'>



""" 
Usage of Random numbers
"""

import random
print(random.randrange(1, 10)) #Prints a random integer between 1 and 9