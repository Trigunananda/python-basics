# Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.
scores = [70, 60, 80, 90, 50]

filtered = []
for score in scores:
    if score >= 70:
        filtered.append(score)
print(filtered)

# Python has a built-in function called filter() that allows you to filter a list (or a tuple) in a more beautiful way.
# filter(fn, list)
# The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements where the fn() returns True.
scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score:score>=70,scores)
print(list(filtered))

# Using the Python filter() function to filter a list of tuples
# Suppose you have the following list of tuples:
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]
# Each element in a list is a tuple that contains the country’s name and population.
# To get all the countries whose populations are greater than 300 million, you can use the filter() function as follows:
populated = filter(lambda country:country[1]>300000000,countries)
print(list(populated))