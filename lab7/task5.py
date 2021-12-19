#. Дана цілочислова прямокутна матриця. Визначити номер рядка, в якому знаходиться сама довша серія однакових елементів
import random
num_rows = int(input('введіть рядок'))
num_columns = int(input('введіть стовпець'))
A = [[random.randint(0, 1) for j in range(num_rows)] for i in range(num_columns)]

count_zero = 0
R = len(A)
C = len(A[0])
for col in range(C):
    values = [r[col] for r in A]
    if 0 in values:
        count_zero += 1

print(A)
print(count_zero)