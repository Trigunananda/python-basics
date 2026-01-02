# The try statement has an optional else clause with the following syntax:
# try:
    # code that may cause errors
# except:
    # code that handle exceptions
# else:
    # code that executes when no exception occurs

# If an exception occurs in the try clause, Python skips the rest of the statements in the try clause and the except statement execute.
# In case no exception occurs in the try clause, the else clause will execute.

# When you include the finally clause, the else clause executes after the try clause and before the finally clause.

# Python try…except…else statement examples
# 1) Using try…except…else statement for control flow
# First, define a function for calculating the (BMI) based on height and weight:
def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2

# Second, define another function for evaluating BMI:
def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'


# Third, define a new main() function that prompts users for entering height and weight, and prints out the BMI result:
def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print('Error! please enter a valid number.')
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')
main()

# 2) Using Python try…except…else and finally example
# The else clause executes right before the finally clause if no exception occurs in the try clause.
fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')

