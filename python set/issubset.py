#  use the Python issubset() method to check if a set is a subset of another set.
# Introduction to the Python issubset() method 

# Suppose that you have two sets A and B. Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.
# issubset() method to check if the set_a is a subset of the set_b:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers))

# By definition, a set is also a subset of itself. The following example returns True

numbers = {1, 2, 3, 4, 5}

print(numbers.issubset(numbers))

# The following example returns False because some elements in the numbers set aren’t in the scores set. In other words, the numbers set is not a subset of the scores set:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(numbers.issubset(scores))

# Using subset operators 
# Besides using the issubset() method, you can use the subset operator (<=) to check if a set is a subset of another set:
# The subset operator (<=) returns True if set_a is a subset of the set_b. Otherwise, it returns False. For example:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = scores <= numbers
print(result)
result = numbers <= numbers
print(result)

# The proper subset operator (<) check if the set_a is a proper subset of the set_b
# set_a < set_b
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result)  # False

# In this example, the set numbers is not a proper subset of itself, therefore, the < operator returns False