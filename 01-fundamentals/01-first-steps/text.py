#Case 1: Using double quotes to include single quotes in the string
print('Hello, "World!"')
english = "I'm a hooman"

#Case 2: Using single quotes to include double quotes in the string
multipleLines = """Hello,
There!"""

print(english)
print(multipleLines)



#Using length function to count the number of characters in a string
word = "elephant"
print(len(word)) #Prints the length of the string, which is 8.



#Using the in operator to check if a substring is present in a string
text = "This course is about Python Fundamentals."
isPython = "Python" in text 
isJavaScript = "JavaScript" not in text

#Checks if the word "Python" is in the text variable
print(isPython) #Prints True, because is indeed present.

#Checks if the word "JavaScript" is not in the text variable
print(isJavaScript) #Prints True, because is indeed not present.



#Using the upper() method to convert a string to uppercase
uppercaseText = text.upper() #Converts the text variable to uppercase
print(uppercaseText)

#Using the lower() method to convert a string to lowercase
lowercaseText = text.lower() #Converts the text variable to lowercase
print(lowercaseText)



#Using the strip() method to remove leading and trailing whitespace from a string
whiteSpaces = "   Hello, World!   "
withoutWhiteSpaces = whiteSpaces.strip()

print(withoutWhiteSpaces) #Prints "Hello, World!" without the leading and trailing whitespace.