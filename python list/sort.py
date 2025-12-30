# Python Sort List
# The sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list
# If a list contains strings, the sort() method sorts the string elements alphabetically.

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()

print(guests)
# uses the sort() method with the reverse=True argument to sort the elements in the guests list in the reverse alphabetical order
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort(reverse=True)
print(guests)

# If a list contains numbers, the sort() method sorts the numbers from smallest to largest
scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)
# To sort numbers from the largest to smallest
scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)
print(scores)

# Sorting a list of tuples 
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
# This sort_key() function accepts a tuple called company and returns the third element.
# Note that the company is a tuple e.g., ('Google', 2019, 134.81). 
# And the company[2] references the revenue like 134.81 in this case.
def sort_key(company):
    return company[2]



# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(companies)

# Using lambda expression
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
companies.sort(key = lambda company:company[2])
print(companies)