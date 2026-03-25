# Variable
i = 1

"""
ADVICE!
Be careful with infinite loops: 
Make sure to include a condition that will eventually become false, 
or use a break statement to exit the loop when necessary.
"""
# While loop to print numbers from 1 to 5
while i <= 5:
    print (i)
    i += 1 # Increment the value of i by 1 in each iteration

print ("Loop has ended")

# Using break statement to exit the loop
while i <= 10:
    print(i)
    if i == 5:
        break # Exit the loop when i is equal to 5
    i += 1 # Increment the value of i by 1 in each iteration

print ("Loop has ended with break statement")

"""
ADVICE!
Be careful with the addition of the increment statement (i += 1) in the loop,
take control of where you place it, as it can affect the output of the loop.
"""
j = 1
while j <= 10:
    j += 1
    print (j)
    #Output will be 2 to 11, because the print statement is executed before the condition is checked again.

print ("Loop has ended with increment before print statement")



# Continue statement to skip the current iteration
k = 0

while k < 10:
    k += 1
    if k == 5:
        continue # Skip the rest of the loop when k is equal to 5
    print (k)
else:
    print ("k is no longer less than 10") # This will be executed when the loop condition becomes false

print ("Loop has ended with continue statement")
