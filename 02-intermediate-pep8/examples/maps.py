numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)


print(numbers)
print(squared_numbers)


def square(num):
    return num ** 2

# Converting conventional for loop to use map() function
# Map helps the performance of the code by applying the function to each item in the iterable without the need for an explicit loop, and it can be more concise and readable.
squared_map = list(map(square, numbers))
print(squared_map)