# Python Tuples
#  a tuple is an immutable list,Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.

rgb = ('red', 'green', 'blue')

print(rgb[0])
print(rgb[1])
print(rgb[2])

# Since a tuple is immutable, you cannot change its elements
rgb = ('red', 'green', 'blue')
# rgb[0] = 'yellow'

# To define a tuple with one element, you need to include a trailing comma after the first element.
numbers = (3,)
print(type(numbers))

# Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple
colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)