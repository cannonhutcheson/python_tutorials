
# imports the random module
import random
# defines the variables that will be used in the function
lower_bound = 1
upper_bound = int(input('How many sides does the die have? '))


def die_roll(lower_bound, upper_bound):
    result = random.randint(lower_bound, upper_bound)
    print_return = input("'print' or 'return'? ")
    if print_return == 'print':
        print(result)
    elif print_return == 'return':
        return result
    else:
        print('Invalid input')
die_roll(lower_bound, upper_bound)
