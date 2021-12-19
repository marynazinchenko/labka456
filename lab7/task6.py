# Дана цілочислова прямокутна матриця. Визначити номер рядка, в якому знаходиться сама довша серія однакових елементів.

import random

num_rows = int(input())
num_columns = int(input())
A = [[random.randint(-10,10) for j in range(num_rows)] for i in range(num_columns)]


top_row = 0
j= 0
unique = 1
while j < num_columns:
    Row_list = A[j]
    row_unique_max = dict((x, Row_list.count(x)) for x in set(Row_list) if Row_list.count(x) > unique)
    if row_unique_max != {}:
        value = row_unique_max.get(list(row_unique_max.keys())[0])
        if  value > unique:
            unique = row_unique_max.get(list(row_unique_max.keys())[0])
            top_row = j
    j+=1
print( "рядок з найб серією: " , top_row)