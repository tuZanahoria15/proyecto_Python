# Variable
word = "Python"

"""
For loop:
A for loop is used to iterate over a sequence (like a list, tuple, string, etc.)
"""

#  1st example: Iterating over a string
for letter in word:
    print (letter) # This will print each letter in the word "Python" on a new line

print ("Loop has ended")


# 2nd example: Iterating over a list + break statement
fuits = ["apple", "orange", "kiwi"]

for fruit in fuits:
    if fruit == "orange":
        break # Exit the loop when the fruit is "orange"
    print (fruit) # This will print each fruit (item) in the list on a new line

print ("Loop has ended with break statement")


# 3rd example: Iterating over a list + continue statement
for fruit in fuits:
    if fruit == "orange":
        continue # Skip the rest of the loop when the fruit is "orange"
    print (fruit) # This will print each fruit (item) in the list on a new line, except for "orange"
else:
    print ("Loop for has ended with continue statement")


print("//////////////////////////////")


"""
Range function:
The range() function is used to generate a sequence of numbers.
It can take one, two, or three arguments:
- range(stop): Generates numbers from 0 to stop-1
- range(start, stop): Generates numbers from start to stop-1
- range(start, stop, step): Generates numbers from start to stop-1, incrementing by step
"""

for i in range(10): # This will generate numbers from 0 to 9
    print (i)

for i in range(1, 5): # This will generate numbers from 1 to 4
    print (i)

for i in range(0, 10, 2): # This will generate even numbers (2+2) from 0 to 8
    print (i)

print("Loop with range function has ended")



# Nested for loops: A for loop inside another for loop
# Two lists to iterate over
colors = ["red", "green", "blue"]
shapes = ["circle", "square", "triangle"]

for color in colors:
    for shape in shapes:
        print (color, shape) # This will print each color with each shape (total of 9 combinations)

print ("Nested loops have ended")


# Using Pass statement in a for loop
for i in range(5):
    pass # This is a placeholder for future code, it does nothing