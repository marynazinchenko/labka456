#Розмістити елементи парних стовпців у порядку зростання
import random

num_rows = int(input())
num_columns = int(input())
A = [[random.randint(-5,5) for j in range(num_rows)] for i in range(num_columns)]
print (A)

R = len(A)
C = len(A[0])
for col in range(C):
    values = [r[col] for r in A]
    if col !=0 and col % 2 == 0:
       values.sort(reverse=True)
       for row in range(R):
           A[row][col] = values.pop()

print (A)