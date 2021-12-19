#Дано типізований файл, який містить цілі числа. Визначити суму додатних елементів використовуючи стек для збереження елементів. Суму елементів дописати у кінець даного файлу.
import math
sum = 0
with open('my.txt') as f:
        for num in f:
            n = int(num)
            if n>0:
                sum += n
f.close()
frecord = open('my.txt', 'wt')
print(sum, file=frecord, sep='', end='')
frecord.close()




