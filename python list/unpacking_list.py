# How to Unpack a List in Python
# Summary: in this tutorial, you’ll learn how to unpack a list in Python to make your code more concise.

# To assign the first, second, and third elements of the list to variables, you may assign individual elements to variables like this:
colors = ['red', 'blue', 'green']

red = colors[0]
blue = colors[1]
green = colors[2]

colors = ['red', 'blue', 'green']

red, blue, green = colors

print(red)
print(green)
print(blue)

# In this example, the number of variables on the left side is the same as the number of elements in the list on the right side.

# If you use a fewer number of variables on the left side, you’ll get an error. For example:
# colors = ['red', 'blue', 'green']
# red, blue = colors
# print(colors)

# Unpacking and packing
colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors

print(cyan)
print(magenta)
print(other)
