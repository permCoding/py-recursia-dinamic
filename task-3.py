'''
Одномерная динамика

Оловянный солдатик
Он ходит по шахматной доске. В начале пути он стоит на линии 1 (не важно на какой вертикали, букве).
У солдатика ограничена длина шага в клетках - d.
Каждый шаг солдатик делает случайной длины в диапазоне [1,d].
Пусть дана размерность доски, например - 4 клетки (доска 4х4) и
максимальная длина шага в клетках, например, 3.
Вопрос: сколько разных способов у солдатика на то, чтобы дойти до края стола?
'''


def get_1(n, m): # простая рекурсия
	if n <= 1:
		return 1
	else:
		count = 0
		for step in range(1, m + 1):
			if step <= n:
				count += get_1(n-step, m)
		return count


def get_2(n, m): # рекурсия с кэшированием - сделать самостоятельно
	pass
	pass
	pass
	return 0


def get_3(n, m): # динамика -
	tab = [0] * (n + 1)
	tab[0] = 1 # солдатик, стоящий на клетке 1 имеет один путь
	for pos in range(n):
		for step in range(1, m + 1):
			if pos + step > n : continue
			tab[pos + step] += tab[pos]
		# print(tab) # для контроля
	return tab[n]


import time

n = 125 # размер доски
n -= 1 # длина пути = размер доски - 1 (так как на 1 клетке уже стоит солдатик)
m = 13 # длина максимального шага

start = time.monotonic()
# print('get_1 = %5d' % (get_1(n, m)))
# print('get_2 = %5d' % (get_2(n, m)))
# print('get_3 = %5d' % (get_3(n, m)))
result = get_3(n, m)
finish = time.monotonic()

dif = finish - start

print('%3d%3d%12d\t%10.3f' % (n, m, result, dif))
