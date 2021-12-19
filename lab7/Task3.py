import random
num_rows = int(input())
num_columns= int(input())
a = [[random.randint(-10, 10) for j in range(num_rows)] for i in range(num_columns)]
b = [[random.randint(-10, 10) for j in range(num_rows)] for i in range(num_columns)]

print(a)
print(b)

result = [[a[i][j] + b[i][j] for j in range
(len(a[0]))] for i in range(len(a))]

for r in result:
    print(r)
