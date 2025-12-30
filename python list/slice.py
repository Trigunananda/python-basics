
# Python List Slice
# Lists support the slice notation that allows you to get a sublist from a list:

# sub_list = list[begin: end: step]

# The following example uses the list slice to get a sublist from the colors list:
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[1:4]
print(sub_colors)

# To get the n-first elements from a list, you omit the first argument:
# list[:n]
# The following example returns a list that includes the first three elements from the colors list:
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[:3]
print(sub_colors)

# Retrieving the n-last elements from a list
# To get the n-last elements of a list, you use the negative indexes.
# For example, the following returns a list that includes the last 3 elements of the colors list:

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[-3:]

print(sub_colors)
# Retrieving every nth element from a list 
# The following example uses the step to return a sublist that includes every 2nd element of the colors list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[::2]
print(sub_colors)

# Reversing a list 
colors = ["red","orange","yellow","green","blue","indigo","violet"]
reversed_colors = colors[::-1]
print(reversed_colors)

# Substituting a part of a list 
# Besides extracting a part of a list, the list slice allows you to change the list element.
# The following example changes the first two elements in the colors list to the new values:
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2]=['black','purple']
print(colors)

# Partially replacing and resizing a list 
# The following example uses the list slice to replace the first and second elements with the new ones and also add a new element to the lis
colors = ["red","orange","yellow","green","blue","indigo","violet"]
print(f"The list has {len(colors)} elements")
colors[0:2]=['black','white','gray']
print(colors)
print(f"The list has {len(colors)} elements")   

# Deleting elements
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
del colors[2:5]
print(colors)