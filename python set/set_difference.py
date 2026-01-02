# The difference between the two sets results in a new set that has elements from the first set which aren’t present in the second set.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
{'Python'}
# Using Python Set difference() method to find the difference between sets 
# set1.difference(s2, s3, ...)

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)

print(s)

# this example shows how to use the set difference() method to find the difference between s2 and s1 sets.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)

print(s)
# Note that the difference() method returns a new set. It doesn’t change the original sets.

#  Using Python set difference operator (-) to find the difference between sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 - s2

print(s)

# The set difference() method vs set difference operator (-)
# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) while the set difference operator (-) only allows sets.

# When you pass iterables to the set difference() method, it’ll convert the iterables to sets before performing the difference operation.
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)

print(new_scores)

# However, if you use the set difference operator (-) with iterables, you’ll get an error:
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores - numbers

# print(new_scores)

# TypeError: unsupported operand type(s) for -: 'set' and 'list'