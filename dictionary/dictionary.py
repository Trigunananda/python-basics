#  Python dictionary type that allows you to create a collection of key-value pairs.
# A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. In fact, you can use a value of any valid type in Python as the value in the key-value pair.

# A key in the key-value pair must be immutable. In other words, the key cannot be changed, for example, a number, a string, a tuple, etc.

# Python uses curly braces {} to define a dictionary. Inside the curly braces, you can place zero, one, or many key-value pairs.
empty_dict = {}
print(type(empty_dict))

# The following example defines a dictionary with some key-value pairs:
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
# Accessing values in a Dictionary
# dict[key]

print(person['first_name'])
print(person['last_name'])

# Using the get() method
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# ssn = person['ssn']

#  Traceback (most recent call last):
#   File "dictionary.py", line 15, in <module>
#     ssn = person['ssn']
# KeyError: 'ssn' 

# ssn = person.get('ssn')
ssn = person.get('ssn', '000-00-0000')
print(ssn)

# Modifying values in a key-value pair
# dict[key] = new_value
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

person['age'] = 26

print(person)

# Removing key-value pairs
# del dict[key]
del person['active']
print(person)

# Looping all key-value pairs in a dictionary
# Python dictionary provides a method called items() that returns an object which contains a list of key-value pairs as tuples in a list.
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person.items())

# To iterate over all key-value pairs in a dictionary, you use a for loop with two variable key and value to unpack each tuple of the list
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key, value in person.items():
    print(f"{key}: {value}")

# Looping through all the keys in a dictionary 
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key in person.keys():
    print(key)    

# In fact, looping through all keys is the default behavior when looping through a dictionary. Therefore, you don’t need to use the keys() method.    
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key in person:
    print(key)

# Looping through all the values in a dictionary 
# The values() method returns a list of values without any keys.    
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for value in person.values():
    print(value)

