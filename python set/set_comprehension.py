# how to use Python set comprehension to create a new set based on an existing one.
# Suppose that you have the following set that consists of three tags:
tags = {'Django', 'Pandas', 'Numpy'}
# To convert the tags in the set to another set of tags in lowercase, you may use the following for loop:
lowercase_tags = set()
for tag in tags:
    lowercase_tags.add(tag.lower())
print(lowercase_tags)

#  you can use the built-in map() function with a lambda expression:
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = set(map(lambda tag:tag.lower(),tags))
print(lowercase_tags)

# To make the code more concise, Python provides you with the set comprehension syntax as follows:
# {expression for element in set if condition}
# Note that the set comprehension returns a new set, it doesn’t modify the original set.
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)

# Python Set comprehension with an if clause example
# Suppose you want to convert all elements of the tags set to lowercase except for the Numpy.
tags = {'Django', 'Pandas', 'Numpy'}
new_tags  = {tag.lower() for tag in tags if tag!= 'Numpy'}
print(new_tags)