#Визначити добуток від’ємних елементів матриці з обома непарними індексами.
import random
num_rows =int(input())
num_columns = int(input())
A = [[random.randint(-10,10) for j in range(num_rows)] for i in range(num_columns)]
print(A)

i = 0
j = 0
result = 1

while  i < num_rows:
    if i == 0 or i%2 > 0:
        while j < num_columns:
            if j == 1 or j%2 > 0:
                if A[i][j] < 0 :
                    result = result * A[i][j]
                    j = j+1
                else:
                    j = j+1
            else: j = j+1
        j=j+1
        i = i+1
    else:
        i = i+1
i = i+1
print (result)