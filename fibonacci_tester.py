
# returns an answer as to whether or not an entered number is a Fibonacci number
def is_fibonacci(number):
	# we need to find these numbers so we can test below 
	test_1 = (5 * number**2 + 4)
	test_2 = (5 * number**2 - 4)
	# if these numbers are perfect squares, then we have a Fibonacci number
	if (test_1**0.5 % 1) == 0 or (test_2**0.5 % 1) == 0:
		print('Number is a Fibonacci number.')
	else:
		print('Number is not a Fibonacci number.')


is_fibonacci(514229)








