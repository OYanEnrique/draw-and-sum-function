from random import randint
from time import sleep

numbers = []

def draw(n_list):
	print('Drawing 5 values ​​from the list: ', end = ' ')
	for c in range (0, 5):
		n = randint(1, 10)
		n_list.append(n)
		print(f'{n}, ', end='', flush=True)
	print('Done!')

def sumeven(n_list):
	sum = 0
	for value in n_list:
		if value % 2 == 0:
			sum += value
	print(f'Adding the even values ​​of {n_list}, we have {sum}')
	
draw(numbers)
sumeven(numbers)