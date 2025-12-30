# Python dictionary comprehension to transform or filter items in a dictionary.
# like a for loop, a dictionary comprehension offers a more expressive and concise syntax when you use it correctly.

# Here is the general syntax for dictionary comprehension:

# {key:value for (key,value) in dict.items() if condition}

# Suppose that you have the following dictionary whose items are stock symbol and price:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
# To increase the price of each stock by 2%, you may come up with a for loop like this:
new_stocks = {}
for symbol,price in stocks.items():
    new_stocks[symbol]=price*1.02
print(new_stocks) 

# The following example shows how to use dictionary comprehension to achieve the same result:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
new_stocks = {symbol : price * 1.02 for (symbol,price) in stocks.items()}
print(new_stocks)

# This dictionary comprehension is equivalent to the for loop counterpart


# Using Python dictionary comprehension to filter a dictionary 
# To select stocks whose prices are greater than 200, you may use the following for loop:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
selected_stocks = {}
for symbol,price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price
print(selected_stocks)        

# The following example uses the dictionary comprehension with an if clause to get the same result:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
selected_stocks = {s:p for(s,p) in stocks.items() if p > 200}
print(selected_stocks)