'''
Двумерная динамика

Путь по городу
Есть двумерная матрица - модель улиц под прямым углом...
Каждая ячейка обозначает стоимость прохода через неё (по улице).
Нужно пройти от левого верхнего угла к правому нижнему.
Ходить можно только по улицам, то есть только вправо или только вниз.
Возвращаться нельзя...

Вопрос: какова минимальная стоимость прохода через город?
Решить задачу:
0) наивно
1) рекурсией
2) динамикой
'''


def get_1(n, m):  # простая рекурсия
	if n == 0 and m == 0:
		return tab[0][0]
	elif n == 0 and m > 0:
		return tab[0][m] + get_1(0, m - 1)
	elif n > 0 and m == 0:
		return tab[n][0] + get_1(n - 1, 0)
	else:
		return tab[n][m] + min(get_1(n, m - 1), get_1(n - 1, m))


def get_2(n, m):  # рекурсия с кэшированием
	pass
	pass
	pass
	return 0


def get_3(n, m):  # динамика - самостоятельно
	pass
	pass
	pass
	return 0


f = open('task-4.txt', 'r')
lines = f.read().split('\n')
f.close()

n, m = map(int, lines[0].split())
tab = []
for row in lines[1:]:
	tab.append(list(map(int, row.split())))

for row in tab:
	print(*row)

print(get_1(0, 0))
print(get_1(1, 1))
print(get_1(0, m-1))
print(get_1(n-1, 0))
print(get_1(n-1, m-1))
