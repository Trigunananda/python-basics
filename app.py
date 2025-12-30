# # define main function to print out something
# def main():
#     i = 1
#     max = 10
#     while (i <= max):
#         print(i)
#         i = i + 1

# # call function main 
# main()

# if (1) and (1) and \
#    (1 == True):
#     print("Continuation of statements")


#     import keyword

# print(keyword.kwlist) 

# s = 'This is a string'
# print(s)
# s = "Another string using double quotes"
# print(s)
# s = ''' string can span
#         multiple line '''
# print(s)

# string = "trigunanada Swain"
# mess = f"hi {string}"
# print(mess)
# print(string[0])
# print(string[1])

# x = 20
# y = 10
# quotient = x / y
# print(quotient)

# value = input('Enter a value:')
# print(value)

# price = input('Enter the price ($):')
# tax = input('Enter the tax rate (%):')
# tax_amount = int(price) * int(tax) / 100
# print(f'The tax amount price is {(tax_amount)}')

# x=5
# y=2
# z=x//y
# print(z)


PRICE = 9.9
RESULT = PRICE > 9 and PRICE < 12
print(RESULT)

price = 9.99
result = not price > 10
print(result)

# age = input("Enter Your age:")
# print(type(age))
# if int(age) >= 18:
#     print("You are eligible to vote!!")
#     print("Let's go and vote")

# age = input("Enter Your age:")
# your_age = int(age) 
# if your_age < 5:
#     ticket_price = 5
# elif your_age <16:
#       ticket_price = 10
# else:
#       ticket_price = 18

# print(f"you will pay ${ticket_price} for the ticket")               

#ternary operator
# ticket_price = 20 if your_age >= 18 else 5
# print(ticket_price)

# for index in range(5):
#      print(index)
# for index in range(1,6,2):
#      print(index)
# for index in range(0,11,2):
#      print(index)

# sum = 0
# for num in range(101):
    #  print(num)   
#      sum += num
# print(sum)       

# command = ''

# while command.lower() != 'quit':
#     command = input('>')
#     print(f"Echo: {command}")

# for index in range(0,10):
#      print(index)  
#      if index == 3:
#         break  
    
# for index in range(10):
#     if index % 2:
#         continue
#     print(index)

# counter = 0
# for index in range(10):
#     counter +=1
#     # Uses if not index % 2: to check if the number is even
#     if not index % 2:
#         continue
#     print(index)   

# counter = 1
# max = 10
# if counter <= max:
#     counter += 1
# else:
#     pass

# def greet(name):
#     print(f"i am {name}")
# greet('John')




celsius_temperature = input("Enter the temperature in celsius:")
print(celsius_temperature,"℃")
celsius = float(celsius_temperature)
farehnit = (celsius * 9 / 5) + 32
print("TEmperature in Farenheit is:",str(farehnit))
print(str(farehnit),"℉")








billAmount_str = input("Enter total bill amount: ")
discount_str = input("Enter discount percentage: ")
bill_amount = float(billAmount_str)
discount_percentage = int(discount_str)
discount_amount = bill_amount * discount_percentage / 100
final_amount = bill_amount - discount_amount
print("The final amount after discount is ₨", final_amount)






