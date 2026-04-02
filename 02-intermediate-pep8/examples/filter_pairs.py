numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)


def is_pair(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


"""
filter() is a built-in function that constructs an iterator from elements of an iterable for which a function returns true. 
In this case, we can use filter() to create an iterator of the even numbers from the list 'numbers' by passing the 'is_pair' function and the 'numbers' list as arguments."""

# Using list(filter()) to create a list of even numbers
# Filter helps the performance of the code by applying the function to each item in the iterable without the need for an explicit loop, and it can be more concise and readable.
pairs_filter = list(filter(is_pair, numbers))
print(pairs_filter)
