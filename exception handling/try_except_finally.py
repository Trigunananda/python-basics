# The try...except statement allows you to catch one or more exceptions in the try clause and handle each of them in the except clauses.

# The try...except statement also has an optional clause called finally:

# try:
    # code that may cause exceptions
# except:
    # code that handle exceptions
# finally:
    # code that clean up

# The finally clause always executes whether an exception occurs or not. And it executes after the try clause and any except clause

# Python try…except…finally statement examples
a = 10
b = 0

try:
    c=a/b
    print(c)
except ZeroDivisionError as error:
    print(error)  
finally:
    print('Finishing Up.')      

# The catch clause in the try...except...finally statement is optional. So you can write it like this:
# try:
    # the code that may cause an exception
# finally:
    # the code that always executes
# Typically, you use this statement when you cannot handle the exception but you want to clean up resources. For example, you want to close the file that has been opened.
