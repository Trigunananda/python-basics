#  how to use the Python isdisjoint() method to check if two sets are disjoint.
# Two sets are disjoint when they have no elements in common. In other words, two disjoint sets are sets whose intersection is an empty set.

# For example, the {1,3,5} and {2,4,6} sets are disjoint because they have no common elements.

# In Python, you use the Set isdisjoint() method to check if two sets are disjoint or not:

# Python isdisjoint() method examples
odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
result = odd_numbers.isdisjoint(even_numbers)
print(result)

# The following example uses the isdisjoint() method to check if the set letters and the set alphanumerics are disjoint

letters = {'A', 'B', 'C'}
alphanumerics = {'A', 1, 2}
result = letters.isdisjoint(alphanumerics)
print(result)

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
result = odd_numbers.isdisjoint(even_numbers)
print(result)

letters = {'A', 'B', 'C'}
result = letters.isdisjoint([1, 2, 3])
print(result)

