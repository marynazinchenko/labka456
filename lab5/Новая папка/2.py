#дано N є n. побудувати алгоритм для визначення к-сть одиниць у числі n
import math
n=int(input('число='))
sum=0
b=str(n)
c=list(b)
print(c)
for el in  (c):
    if el=='1':
        sum=sum + 1
print(sum)

