# A list is an ordered collection of items.
numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
print(numbers[1])
print(numbers[-1])
# A list is dynamic. It means that you can modify elements in the list, add new elements to the list, and remove elements from a list.
numbers[0]=10
print(numbers)
numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1]*10

print(numbers)
# Adding elements to the list 
# The append() method appends an element to the end of a list
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)

print(numbers)

# The insert() method adds a new element at any position in the list.
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)
# Removing elements from a list 
# The del statement allows you to remove an element from a list by specifying the position of the element.
numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]

print(numbers)

# The pop() method removes the last element from a list and returns that element:

numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()

print(last)
print(numbers)

# To pop an element by its position
numbers = [1, 3, 2, 7, 9, 4]

second = numbers.pop(1)

print(second)
print(numbers)

# To remove an element by value, you use the remove() method. Note that the remove() method removes only the first element it encounters in the list.
numbers = [1, 3, 2, 7, 9, 4, 9]

numbers.remove(9)
print(numbers)