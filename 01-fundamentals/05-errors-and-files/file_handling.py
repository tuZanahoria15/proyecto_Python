"""
File Handling:
In Python, you can handle files using the built-in `open()` function. 
This function allows you to read from and write to files on your computer. 

Modes:
* Read (r): Opens a file for reading. 
[The file must exist.]

* Write (w): Opens a file for writing. If the file already exists, it will be overwritten. 
[If it does not exist, a new file will be created.]

* File Creation (X): Opens a file for exclusive creation. 
[If the file already exists, an error will be raised.]


!!!
It's important to execute this program in the right directory where the file is located.
Otherwise, the file will not be found, and a FileNotFoundError will be raised.
On the console type: cd .\05-errores-y-archivos\
"""

## READING FILES
# Using (r) read mode to open a file and read its content
try:
    f = open("file.txt", "r")  # Open the file in read mode
    print(f.readline()) # Read and print the first line of the file
    f.close() # Close the file to free up system resources

except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")


# Using "WITH" statement to handle files, and "ENCODING" to avoid potential issues with special characters
try:
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.readline()) # Read and print the first line of the file
        print(f.readline()) # Read and print the second line of the file
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")



## WRITING FILES
# Using (w) write mode to create a new file or overwrite an existing one
try:
    with open("file.txt", "w") as f:
        f.write("Hello, this is a new line in the file.\n") # Write a line
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.readline()) # Read and print the line we just wrote to the file
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")


# Using (a) append mode to add content to the file without overwriting it
try:
    with open("file.txt", "a") as f:
        f.write("\n") # Add a newline before appending the new line for better readability
        f.write("Hello, this is a new line in the file.\n") # Write a line
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.read()) # Read and print the entire content of the file to see the appended line
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")



## CREATING FILES
# Using (x) exclusive creation mode to create a new file.
try:
    with open("file.txt", "r") as f:
        print(f.readline()) # Read and print the first line of the file
        print(f.readline()) # Read and print the second line of the file
except FileNotFoundError:
    open("file.txt", "x") # Create the file if it does not exist
    print("The file 'file.txt' was not found, but it has been created.")

try:
    with open("file.txt", "a") as f:
        f.write("Hello, this is a new line since the file was created.\n") # Write a line
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.read()) # Read and print the entire content of the file to see the appended line
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")