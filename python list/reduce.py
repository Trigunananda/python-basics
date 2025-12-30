# How to Use the Python Reduce() function to Reduce a List into a Single Value
scores = [75, 65, 80, 95, 50]
# And to calculate the sum of all elements in the scores list, you can use a for loop like this:
total = 0
for score in scores:
    total += score
print(total)        


# Introduction the Python reduce() function
# Python offers a function called reduce() that allows you to reduce a list in a more concise way

# reduce(fn,list)

# Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module
# To use the reduce() function, you need to import it from the functools module using the following statement at the top of the file:

# from functools import reduce
from functools import reduce
def sum(a,b):
    print(f"a={a},b={b},a+b={a+b}")
    return a + b

scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

from functools import reduce
scores = [75, 65, 80, 95, 50]
total = reduce(lambda a,b:a+b,scores)
print(total)