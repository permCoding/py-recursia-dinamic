# py-recursia-dinamic
## Лекция - Алгоритмы рекурсивные и динамического программирования  
  
_С замером времени исполнения - time.monotonic()_  

__task-1 Числа Фибоначчи__

* get_1(n): # простая рекурсия
* get_2(n): # рекурсия с кэшированием
* get_3(n): # динамика с затратами памяти
* get_4(n): # динамика без затрат памяти

---  

__Одномерная динамика__  


task-1  
__Числа Фибоначчи__  


task-2  
__Оловянный солдатик-2__  
Он ходит по шахматной доске. В начале пути он стоит на линии 1 (не важно на какой вертикали, букве).
Каждый шаг он делает случайной ногой, НО, одна нога ходит на 1 клетку, а другая на 2 клетки...
Пусть дана размерность доски, например - 4 клетки (доска 4х4).  
Вопрос: сколько разных способов у солдатика на то, чтобы дойти до края стола?  
  
  
task-3  
__Оловянный солдатик-d__  
Он ходит по шахматной доске. В начале пути он стоит на линии 1 (не важно на какой вертикали, букве).
У солдатика ограничена длина шага в клетках - d.
Каждый шаг солдатик делает случайной длины в диапазоне [1,d].
Пусть дана размерность доски, например - 4 клетки (доска 4х4) и максимальная длина шага в клетках, например, 3.  
Вопрос: сколько разных способов у солдатика на то, чтобы дойти до края стола?  
  
---  
  
__Двумерная динамика__
  
  
task-4  
__Путь по городу__  
Есть двумерная матрица - модель улиц под прямым углом...
Каждая ячейка обозначает стоимость прохода через неё (по улице).
Нужно пройти от левого верхнего угла к правому нижнему.
Ходить можно только по улицам, то есть только вправо или только вниз.
Возвращаться нельзя...  
Вопрос: какова минимальная стоимость прохода через город?  
Решить задачу:  
1) рекурсией  
2) динамикой  
3) наивным методом  
  
- измеряем и сравниваем время исполнения...  

---
