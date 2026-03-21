t = True
f = False

print(t) 
print(f)

print(5 > 3) #Prints True because 5 is greater than 3
print(5 < 3) #Prints False because 5 is not less than 3

print(type(t)) #Prints <class 'bool'> because t is a boolean variable
print(type(f)) #Prints <class 'bool'> because f is a boolean variable


"""
Casting to boolean values
"""
#CASES WITH FALSE BOOLEAN VALUES
print(bool("")) #Prints False because an empty string is considered false in a boolean context
print(bool(0)) #Prints False because 0 is considered false in a boolean context
print(bool([])) #Prints False because an empty list is considered false in a boolean context
print(bool(None)) #Prints False because None is considered false in a boolean context

#CASES WITH FALSE BOOLEAN VALUES
print(bool("Hello")) #Prints True because a non-empty string is considered true in a boolean context
print(bool(123)) #Prints True because any non-zero value is considered true in a boolean context
print(bool("apple","banana")) #Prints True because a non-empty tuple is considered true in a boolean context



#Using the isinstance() function to check if a variable is an instance of the bool class
x = 123
print(isinstance(x, int)) #Prints True because x is an instance of the int class
print(isinstance(x, bool)) #Prints False because x is not an instance of the bool class
