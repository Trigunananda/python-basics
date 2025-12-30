# How to Use a For Loop to Iterate over a List
# In this syntax, the for loop statement assigns an individual element of the list to the item variable in each iteration.
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

# Sometimes, you may want to access indexes of elements inside the loop. In these cases, you can use the enumerate() function.  
# The enumerate() function returns a tuple that contains the current index and element of the list.  
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for item in enumerate(cities):
    print(item)

# To access the index, you can unpack the tuple within the for loop statement like this:
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for index,city in enumerate(cities):
    print(f"{index}:{city}") 
# The enumerate() function allows you to specify the starting index which defaults to zero.

# The following example uses the enumerate() function with the index that starts from one:    

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for index,city in enumerate(cities,1):
        print(f"{index}: {city}")