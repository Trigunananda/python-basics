
def greetName(name):
    return f"Hi {name}"
greeting = greetName('Triguna')
print(greeting)

def sum(a,b):
    return a+b
total = sum(10,20)
print(total)

def greetDefault(name,message='HI'):
    return f"{message} {name}"
result = greetDefault('TNs')
print(result)

# normal argument
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
print(f'positional argument{net_price: .2f}')

# normal swapping argument
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(0.1,100)
print(f'after swap positional argument{net_price: .2f}')


# use of keyword argument
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(
    price=100, 
    discount=0.1
)

print(f'keyword argument{net_price: .2f}')

# swap the keyword argument
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(
    discount=0.1,
    price=100,
)

print(f'after swap keyword argument{net_price: .2f}')


# function by mixing positional and keyword arguments
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(
    100, 
    discount=0.1
)

print(f'{net_price: .2f}')

# uses the default values for tax and discount parameters and positional arguments:
def get_net_price(price, tax_rate=0.07, discount=0.05):
    discounted_price = price * (1 - discount)  
    net_price = discounted_price * (1 + tax_rate)  
    return net_price

net_price = get_net_price(100)
print(f'{net_price: .2f}')

#  error because it uses the positional argument after a keyword argument:
# SyntaxError: positional argument follows keyword argument
# def get_net_price(price, tax_rate=0.07, discount=0.05):
#     discounted_price = price * (1 - discount)
#     net_price = discounted_price * (1 + tax_rate)
#     return net_price
# net_price = get_net_price(
#     100, 
#     tax_rate=0.08, 
#     0.06
# )
# print(f'{net_price:.2f}')

# To fix this, you need to use the keyword argument for the third argument like this:
def get_net_price(price, tax_rate=0.07, discount=0.05):
    discounted_price = price * (1 - discount)  
    net_price = discounted_price * (1 + tax_rate)  
    return net_price

net_price = get_net_price(
    100, 
    tax_rate=0.08, 
    discount=0.06
)

print(f'{net_price: .2f}')

# Recursive Function
def count_down(start):
    print(start)
    next = start - 1
    if next > 0:
        count_down(next)
count_down(3)       

#  for loop with the range() function
def sum(n):
    total = 0
    for index in range(n+1):
        total += index
    return total    
result = sum(100)
print(result)





# farehnit = input("Enter The temperature:")
# farehnit_value = float(farehnit)
# celsius = (farehnit_value-32) * 5/9
# print("The value in celsius:",celsius)

# recursive version of the sum() function:
def sum(n):
    if n>0:
        return n + sum(n-1)
    return 0
result = sum(100)
print(result)

#  use the ternary operator, the sum() will be even more concise
def sum(n):
    return n + sum(n-1) if n > 0 else 0
result = sum(100)
print(result)

# Python Lambda Expressions  In Python, you can pass a function to another function or return a function from another function.
# passing function without using lambda
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John


# By using lambda expressions
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)
full_name = get_full_name(
    'Trigunananda',
    'Swain',
    lambda first_name, last_name:f"{first_name} {last_name}"
    )
print(full_name)
full_name = get_full_name(
    'Trigunananda',
    'Swain',
    lambda first_name, last_name:f"{last_name} {first_name}"
    )
print(full_name)

# Functions that return a function example
def time(n):
    return lambda x : x * n
double = time(2)
result = double(2)
print(result)
result = double(3)
print(result)

# Python lambda in a loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())

# Python Function Docstrings : how to use docstrings to add documentation to a function.
# you can use the help() function to find the documentation of the add() function:
def add(a, b):
    "Return the sum of two arguments"
    return a + b
help(add)
# you use multi-line docstrings:
def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

help(add)
# Python stores the docstrings in the __doc__ property of the function.
def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

print(add.__doc__)