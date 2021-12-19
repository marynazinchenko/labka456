
import random

num_rows = 3;
num = int(input("Впровадьте ціле число "))
matrix = [[0 for j in range(num_rows)] for i in range(num_rows)]
row = 0

while row < num_rows:
    column = 0
    while column < num_rows:
        i = random.randint(1, num)
        j = random.randint(-10, num)
        if i * j < 3:
            matrix[row][column] = i + j
            column += 1
        else:
            matrix[row][column] = ((-1) ^ i) * j
            column += 1
    row += 1

a = matrix[0][0]
a_row = 0
row = 0

while row < num_rows:
    if matrix[row][row] > a:
        a = matrix[row][row]
        a_row = row
        row += 1
    else:
        row += 1

r_sum = matrix[a_row][0]
row_column = 1

while row_column < num_rows:
    r_sum = r_sum * matrix[a_row][row_column]
    row_column += 1

print(matrix)
print(a)
print(r_sum)
