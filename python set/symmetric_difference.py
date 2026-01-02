# The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# The symmetric difference of the s1 and s2 sets returns in the following set:

{'C#', 'Python'}

# Using the symmetric_difference() method to find the symmetric difference of sets 
# The Set type has the symmetric_difference() method that returns the symmetric difference of two or more sets:
# new_set = set1.symmetric_difference(set2, set3,...)

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.symmetric_difference(s2)

print(s)

# Note that the symmetric_difference() method returns a new set and doesn’t modify the original sets


# Using the symmetric difference operator(^) to find the symmetric difference of sets
# The following example shows how to apply the symmetric difference operator (^) to the s1 and s2 sets:
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1 ^ s2

print(s)

# The symmetric_difference() method vs symmetric difference operator (^)
# The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.

# If the iterables aren’t sets, the method will convert them to sets before returning the symmetric difference of them.

scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)

print(new_set)

# However, the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error
scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores ^ ratings

print(new_set)

# TypeError: unsupported operand type(s) for ^: 'set' and 'list'

