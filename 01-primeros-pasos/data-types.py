# Strings (Text data type)
singleQuotes = 'This is a text'
doubleQuotes = "This is a text"
tripleQuotes = """Triple Quotes"""  
# Triple quotes can also be used for strings, but they are often used for multi-line strings or docstrings.    

print(singleQuotes) #Prints the value of singleQuotes
print(doubleQuotes) #Prints the value of doubleQuotes
print(tripleQuotes) #Prints the value of tripleQuotes


# (Numbers data type)
a = 1 # Integer
b = 3.14 # Float
c = 5 + 2j # Complex number, where 5 is the real part and 2j is the imaginary part

print(a)
print(b)
print(c)


# Lists (List data type)
myList = [0,1,2,3,4,5] # Elements can change 


# Tuples (Tuple data type)
myTuple = ("a","b","c") # Elements cannot change


# Dictionaries (Dictionary data type)
diccionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# Sets (Set data type)
mySet = {1, 1, 2, 2, 3} # Unordered collection of unique elements
print(mySet) #Prints the unique elements of the set, which are 1, 2, and 3.


# Booleans (Boolean data type)
isTrue = True
isFalse = False