# This simple calculator allows the user to do arithmatic operations such as addition, subtraction, multiplication,
# division, and exponent operations. Simply run the code and the function simple_calc() will take input. 


given_num_1 = float(input('Enter your first number: '))
operator = input('Enter the sign of the operation you would like \n'
                 'to conduct:     ')
given_num_2 = float(input('Enter your second number: '))

def simple_calc():
    if operator == '+':
        print(given_num_1 + given_num_2)
    elif operator == '*':
        print(given_num_1 * given_num_2)
    elif operator == '-':
        print(given_num_1 - given_num_2)
    elif operator == '/':
        print(given_num_1 / given_num_2)
    elif operator == '**' or operator == '^':
        print(given_num_1 ** given_num_2)
    else:
        print('Unsupported Action!')
simple_calc()