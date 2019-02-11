# Practice using generators

import tkinter
import statistics


def fibonacci_number(n: int):
	if n < 2:
		return n
	else:
		return fibonacci_number(n - 1) + fibonacci_number(n - 2)


number_fib_nums = int(input("Enter how many numbers you want for a Fibonacci sequence: "))
fibo_list = []
for i in range(number_fib_nums):
	fibo_list.append(fibonacci_number(i))

print(fibo_list)

