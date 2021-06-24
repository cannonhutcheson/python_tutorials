
try:
    test_num = int(input('Enter your test integer here: '))
except ValueError:
    print('Please enter an integer.')

def odd_even(test_num):
    if test_num != 0 and test_num % 2 == 0:
        print('Number is even.')
    elif test_num != 0 and test_num % 2 != 0:
        print('Number is odd.')
    elif test_num == 0:
        print('Zero is not an odd/even number.')
try:
    odd_even(test_num)
except NameError:
    print('')



