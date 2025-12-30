#  Python List comprehensions that allow you to create a new list from an existing one
numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)

# To make the code more concise, you can use the built-in map() function with a lambda expression:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number**2, numbers))
print(squares)

# The following shows how to use list comprehension to make a list of squares from the numbers list:
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)

# The following shows the basic syntax of the Python list comprehension:
# [output_expression for element in list]

# Python list comprehension with if condition
# The following shows a list of the top five highest mountains on Earth:
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
# To get a list of mountains where the height is greater than 8600 meters, you can use a for loop or the filter() function with a lambda expression like this:
highest_mountains = list(filter(lambda mountain:mountain[1]>8600,mountains))
print(highest_mountains)


# Like the map() function, the filter() function returns an iterator. Therefore, you need to use the list() function to convert the iterator to a list.

# Python List comprehensions provide an optional predicate that allows you to specify a condition for the list elements to be included in the new list:

# [output_expression for element in list if condition]
# This list comprehension allows you to replace the filter() with a lambda
highest_mountains = [m for m in mountains if m[1] > 8600]
print(highest_mountains)