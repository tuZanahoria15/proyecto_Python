"""
Usage of extracting characters from a string using indexing.
"""
#Index -> 0
text = "Good bye"
print(text[0])  # Prints "G"

#Index -> 1
print(text[1])  # Prints "o"

#Index -> 2
print(text[2])  # Prints "o"

#Index -> 3
print(text[3])  # Prints "d"

#Index -> 4
print(text[4])  # Prints " "

#Index -> 5
print(text[5])  # Prints "b"

#Index -> 6
print(text[6])  # Prints "y"

#Index -> 7
print(text[7])  # Prints "e"



"""
Usage of slicing to extract a portion of the string.
"""
print(text[0:2]) #Prints "Go", which is the substring from index 0 to index 2 (3 is not included).
print(text[:4]) #Prints "Good", which is the substring from the beginning of the string to index 3.
print(text[5:8]) #Prints "bye", which is the substring from index 5 to index 7 (8 is not included).



"""
Usage of replace() method to replace a substring with another substring.
"""
course = "This is a course about JavaScript."
course = course.replace("JavaScript", "Python")
#Replaces anytime the word "JavaScript" appears in the course variable with the word "Python".

print(course) #Prints "This is a course about Python".



"""
Usage of split() method to split a string into a list of substrings based on a specified separator.
"""
dividedText = course.split() #Splits the course variable into a list of words using the default separator, which is whitespace.

#Useful whenever we want to use list methods to manipulate the string
print(dividedText)



"""
Seeking for a word and using the lower() method to make the search case-insensitive.
"""
text2 = "This text has UPPERCASE and lowercase letters."

print("uppercase" in text2) #Prints False because the word "uppercase" is not in the text2 variable, since it is written in lowercase.
print("uppercase".lower() in text2.lower()) #Prints True because we are converting both the word "uppercase" and the text2 variable to lowercase before checking if it is present.