# Об’єкт “Матриця”
# поля
# для зберігання елементів матриці;
# для зберігання розмірності матриці;
# методи
# введення елементів матриці;
# виведення елементів матриці;
# знаходження найбільшого елемента;
# знаходження найменшого елемента.

import random

class Matrixx:
    def __init__(self, from_, to_, row_num, col_num):
        self.from_ = from_
        self.to_ = to_
        self.row_num = row_num
        self.col_num = col_num

    def create_matrixx(self):
        A = [[random.randint(self.from_, self.to_) for j in range(self.row_num)] for i in range(self.col_num)]
        print(A)
        print("Максимальне число матриці: ", max(map(max, A)))
        print("Мінімальне число матриці: ", min(map(min, A)))

input_data = Matrixx(-6, 5, 6, 3)
input_data.create_matrixx()