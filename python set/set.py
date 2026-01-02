# A Python set is an unordered list of immutable elements. It means:
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.
# To define a set in Python, you use the curly brace {}

skills = {'Python programming', 'Databases', 'Software design'}
skills = set()

if not skills:
    print('Empty sets are falsy')

# In fact, you can pass an iterable to the set() function to create a set. For example, you can pass a list, which is an iterable, to the set() function like this:

skills = set(['Problem solving','Critical Thinking'])
print(skills)   

# If an iterable has duplicate elements, the set() function will remove them. For example:
characters = set('letter')
print(characters)

# Getting sizes of a set
# len(set)

ratings = {1, 2, 3, 4, 5}
size = len(ratings)
print(size) 

# Checking if an element is in a set
ratings = {1, 2, 3, 4, 5}
rating = 1
if rating in ratings:
     print(f'The set contains {rating}')

# To negate the in operator, you use the not operator. 
ratings = {1, 2, 3, 4, 5}
rating = 6
if rating not in ratings:
       print(f'The set does not contain {rating}')

# Adding elements to a set     
skills = {'Python programming', 'Software design'}
skills.add('Problem solving')
print(skills)

# Removing an element from a set 
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.remove('Software design')
print(skills)       


# If you remove an element that doesn’t exist in a set, you’ll get an error (KeyError). For example:
skills = {'Problem solving', 'Software design', 'Python programming'}
# skills.remove('Java')

# To avoid the error, you should use the in operator to check if an element is in the set before removing it:
skills = {'Problem solving', 'Software design', 'Python programming'}
if 'Java' in skills:
    skills.remove('Java')
print(skills)    

# To make it more convenient, the set has the discard() method that allows you to remove an element. And it doesn’t raise an error if the element is not in the list:
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.discard('Java')

print(skills)

# Returning an element from a set
# To remove and return an element from a set, you use the pop() method.

# Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.

# If you execute the following code multiple times, it’ll show a different value each time:



skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.pop()

print(skills)

# Removing all elements from a set
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.clear()

print(skills)

# Frozen a set
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)
print(skills)

# After that, if you attempt to modify elements of the set, you’ll get an error:

# skills = {'Problem solving', 'Software design', 'Python programming'}
# skills = frozenset(skills)\

# skills.add('Django')

# Looping through set elements
skills = {'Problem solving', 'Software design', 'Python programming'}
for skill in skills:
     print(skill)

# To access the index of the current element inside the loop, you can use the built-in enumerate() function     
skills = {'Problem solving', 'Software design', 'Python programming'}
for index,skill in enumerate(skills):
     print(f"{index}.{skill}")

# By default, the index starts at zero. To change this, you pass the starting value to the second argument of the enumerate() function. For example: 
skills = {'Problem solving', 'Software design', 'Python programming'}

for index, skill in enumerate(skills, 1):
    print(f"{index}.{skill}")

