# дано n чисел x1 x2 x3 ... xn.  Знайти найбыльше серед них.



a = []
n = int(input('к-сть елементів='))
for i in range(n):
     a.append(int(input('значення елементів')))
print('максимальне значення{0}'.format(max(a)))
