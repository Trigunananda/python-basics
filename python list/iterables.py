# In Python, an iterable is an object that includes zero, one, or many elements. An iterable has the ability to return its elements one at a time.

# Because of this feature, you can use a for loop to iterate over an iterable.

# In fact, the range() function is an iterable because you can iterate over its result:
for index in range(3):
    print(index)
# Also, a string is an iterable because you can use a for loop to iterate over it:
str = 'Iterable'    
for ch in str:
    print(ch)
# Lists and tuples are also iterables because you can loop over them. For example:
ranks = ['high', 'medium', 'low']
for rank in ranks:
    print(rank)    

# What is an iterator 
# An iterable can be iterated over. And an iterator is the agent that performs the iteration.

# To get an iterator from an iterable, you use the iter() function. For example:    

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)
# Once you have the iterator, you can get the next element from the iterable using the next() function:
color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

# If there isn’t any more element and you call the next() function, you’ll get an exception.
# color = next(colors_iter)
# print(color)


colors = ['red', 'green', 'blue']
iterator = iter(colors)
for color in iterator:
    print(color)