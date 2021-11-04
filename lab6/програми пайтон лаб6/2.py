
import math
sum = 0
V=[]
n=int(input("Input number"))
for i in range(1,n+1):
    a = math.pow(-1,i) * i
    factorial = 1
    while i> 1:
        factorial *= i
        i -= 1
    z = round(a/factorial,4)
    V.append(z)
print(V)
for y in V:
    if y > 0:
        sum =sum +y
print ('сума всіх додатніх значень= {0} '.format(sum))