# how to use the Python try...except statement to handle exceptions gracefully.

# In Python, there’re two main kinds of errors: syntax errors and exceptions.
# current = 1
# if current < 10
# current += 1

# If you attempt to run this code, you’ll get the following error:
# File "d:/python/try-except.py", line 2
#     if current < 10
#                   ^
# SyntaxError: invalid syntax

# Exceptions 
# Even though when your code has valid syntax, it may cause an error during execution

# In Python, errors that occur during the execution are called exceptions. The causes of exceptions mainly come from the environment where the code executes. For example:

# Reading a file that doesn’t exist.
# Connecting to a remote server that is offline.
# Bad user inputs.

# When an exception occurs, the program doesn’t handle it automatically. This results in an error message

# get input net sales
# print('Enter the net sales for')

# previous = float(input('- Prior period:'))
# current = float(input('- Current period:'))

# # calculate the change in percentage
# change = (current - previous) * 100 / previous

# # show the result
# if change > 0:
#     result = f'Sales increase {abs(change)}%'
# else:
#     result = f'Sales decrease {abs(change)}%'

# print(result)


# Enter the net sales for
# - Prior period:100
# - Current period:120'
# Traceback (most recent call last):
#   File "d:/python/try-except.py", line 5, in <module>
#     current = float(input('- Current period:'))
# ValueError: could not convert string to float: "120'"

# Handling exceptions
# To make the program more robust, you need to handle the exception once it occurs. In other words, you need to catch the exception and inform users so that they can fix it.
# A good way to handle this is not to show what the Python interpreter returns. Instead, you replace that error message with a more user-friendly one.
# you can use the Python try...except statement:
# try:
    # code that may cause error
# except:
    # handle errors

# The try...except statement works as follows:

# The statements in the try clause execute first.
# If no exception occurs, the except clause is skipped and the execution of the try statement is completed.
# If an exception occurs at any statement in the try clause, the rest of the clause is skipped and the except clause is executed.
# try:
#     print('Enter the net sales for')

#     previous = float(input('- Prior period:'))
#     current = float(input('- Current period:'))

#     # calculate the change in percentage
#     change = (current - previous) * 100 / previous

#     # show the result
#     if change > 0:
#         result = f'Sales increase {abs(change)}%'
#     else:
#         result = f'Sales decrease {abs(change)}%'

#     print(result)   
# except:
#       print('Error! Please enter a number for net sales.')     

# However, if you enter zero for the net sales of the prior period:

# Enter the net sales for
# - Prior period:0
# - Current period:100
# Code language: Shell Session (shell)
# … you’ll get the following error message:

# Traceback (most recent call last):
#   File "d:/python/try-except.py", line 9, in <module>
#     change = (current - previous) * 100 / previous
# ZeroDivisionError: float division by zero      

# Handling multiple exceptions
# The try...except allows you to handle multiple exceptions by specifying multiple except clauses:
# try:
#     # code that may cause an exception
# except Exception1 as e1:
#     # handle exception
# except Exception2 as e2:
#     # handle exception
# except Exception3 as e3:
#     # handle exception 

try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')

# It’s a good practice to catch other general errors by placing the catch Exception block at the end of the list:
try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)

