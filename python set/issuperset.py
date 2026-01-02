#  Python issuperset() method to check if a set is a superset of another
# Python issuperset() method examples 
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = numbers.issuperset(scores)
print(result)

# A set is also a superset of itself. For example:
numbers = {1, 2, 3, 4, 5}
result = numbers.issuperset(numbers)

print(result)

# The scores set is not a subset of the numbers set therefore the following example returns False
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores.issuperset(numbers)

print(result)


# Using superset operators (>=)
# The >= operator returns True if the set_a is a superset of the set_b. Otherwise, it returns False. For example:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers >= scores
print(result)  # True

result = numbers >= numbers
print(result)  # True

# To check if a set is a proper superset of another set, you use the > operator:
# set_a > set_b

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers > scores
print(result)  # True

result = numbers > numbers
print(result)  # True

# In this example, the set numbers is not a proper superset of itself, therefore, the > operator returns False.
