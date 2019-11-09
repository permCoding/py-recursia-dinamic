'''
числа Фибоначчи
'''

# 0 1 1 2 3 5 8 13
def get_1(n): # простая рекурсия
	if n < 3:
		return 1
	else:
		return get_1(n-1) + get_1(n-2)


import time

for i in range(20, 35):
	start = time.monotonic()
	result = get_1(i)
	finish = time.monotonic()

	dif = (finish - start)

	print('%d\t%d\t%.3f с' % (i, result, dif))