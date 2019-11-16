'''
числа Фибоначчи
'''

# 0 1 1 2 3 5 8 13

def get_1(n): # простая рекурсия
	if n < 3:
		return 1
	else:
		return get_1(n-1) + get_1(n-2)


tab = []
def get_2(n): # рекурсия с кэшированием
	if n < 3:
		return 1
	else:
		if tab[n-1] == 0:
			tab[n-1] = get_2(n-1)
		return tab[n-1] + tab[n-2]

tab = [0, 1]
def get_3(n): # динамика с затратами памяти
	for i in range(2,n+1):
		tab[i] = tab[i-1] + tab[i-2]
	return tab[n]


def get_4(n):  # динамика без затрат памяти
	a = b = 1
	for _ in range(3, n+1):
		a, b = b, a + b
	return b


import time

for i in range(1, 35):
	start = time.monotonic()
	# result = get_1(i)
	# tab = [0] * i; tab[1] = 1; result = get_2(i)
	# print(tab)
	tab = [0, 1] + [0] * i;	result = get_3(i)
	result = get_4(i)
	finish = time.monotonic()

	dif = (finish - start)

	print('%d\t%d\t%.3f с' % (i, result, dif))
