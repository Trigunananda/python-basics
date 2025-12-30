# When working with a list (or a tuple), you often need to transform the elements of the list and return a new list that contains the transformed element.

# Suppose, you want to double every number in the following bonuses list:

# To do it, you can use a for loop to iterate over the elements, double each of them, and add it to a new list like this

bonuses = [100, 200, 300]

new_bonuses = []
for bonus in bonuses:
    new_bonuses.append(bonus*2)
print(new_bonuses)   

# The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.
# map(fn, list)
def double(bonus):
    return bonus * 2
bonuses = [100,200,300]
iterator = map(double,bonuses)
print(list(iterator))

# Or you make this code more concise by using a lambda expression like this:
bonuses = [150,250,350]
iterator = map(lambda bonus : bonus * 2,bonuses)
# you can convert an iterator to a list by using the the list() function
print(list(iterator))

# Using the Python map() function with a list of strings
names = ['david', 'peter', 'jenifer']
new_names = map(lambda name : name.capitalize(),names)
print(list(new_names))

# Using the Python map() function with a list of tuples
# Suppose that you have the following shopping cart represented as a list of tuples:
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
# And you need to calculate the tax amount for each product with a 10% tax. In addition, you need to add the tax amount to the third element of each item in the list.
# In order to do so, you can use the map() function to create a new element of the list and add the new tax amount to each like this:
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
TAX = 0.1
carts = map(lambda cart : [cart[0],cart[1],int(cart[1] * TAX)],carts)
print(list(carts))