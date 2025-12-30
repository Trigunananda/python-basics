# To find the index of an element in a list, you use the index() function.

# The following example defines a list of cities and uses the index() method to get the index of the element whose value is 'Mumbai':
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
result = cities.index('Mumbai')
print(result)
# However, if you attempt to find an element that doesn’t exist in the list using the index() function, you’ll get an error.
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

# result = cities.index('Osaka')
# print(result)
# ValueError: 'Osaka' is not in list

# To fix this issue, you need to use the in operator.

# The in operator returns True if a value is in the list. Otherwise, it returns False.

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Cairo'
if city in cities:
    result = cities.index(city)
    print(f"The {city} an index of {result}")
else:
    print(f"The {city} does not exist in the list")
