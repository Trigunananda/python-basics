# The intersection() method and & operator have the same performance
# When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.
s1 = {'Python', 'Java','C++'}
s2 = {'C#', 'Java', 'C++' }
# The intersection of these two sets returns a new set that contains two elements 'Java' and 'C++'
s = {'Java', 'C++'}

# Using Python set intersection() method to intersect two or more sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)

print(s)

# Using Python set intersection (&) operator to intersect two or more sets 
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1 & s2

print(s)

# Set intersection() method vs set intersection operator (&)
# The set intersection operator only allows sets, while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.

# If you pass iterables to the intersection() method, it’ll convert the iterables to set before intersecting them.

# However, the set intersection operator (&) will raise an error if you use it with iterables.

# The following example uses the intersection() method to intersect a set with a list:

numbers = {1, 2, 3}
scores = [2, 3, 4]
numbers = numbers.intersection(scores)
print(numbers)

# If you use the set intersection operator (&) instead, you’ll get an error:
numbers = {1, 2, 3}
scores = [2, 3, 4]

numbers = numbers & scores

# print(numbers)

# TypeError: unsupported operand type(s) for &: 'set' and 'list'