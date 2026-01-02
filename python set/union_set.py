# The union of two sets returns a new set that contains distinct elements from both sets.
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
# The union of the s1 and s2 sets returns the following set:
{'Java','Python', 'C#'}

# The following example shows how to union the s1 and s2 sets:
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1.union(s2)
print(s)

# Union sets using union() method
# new_set = set.union(another_set, ...)

# Union sets using the | operator
# The set union operator (|) returns a new set that consists of distinct elements from both set1 and set2.
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1 | s2

print(s)

# The union() method vs. set union operator
# The union() method accepts one or more iterables, converts the iterables to sets, and performs the union.
# The following example shows how to pass a list to the union() method:

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)

# However, the union operator (|) only allows sets, not iterables like the union() method.
rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates | ranks
# TypeError: unsupported operand type(s) for |: 'set' and 'list'
# In conclusion, the union() method accepts the iterables while the union operator only allows sets