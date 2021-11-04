# Обчислити площу та периметр прямокутника, довжини сторін якого задаються
#Ввести необхідні данні
'''
 перша сторона - float - side1_rectangle
друга сторона - float - side2_rectangle
пеример -float -perimeter
площа -float -area
'''
#вводимо дані
side1_rectangle = float(input('перша сторона '))
side2_rectangle = float(input('друга сторона '))

#обчислюємо
perimeter = 2*(side1_rectangle+side2_rectangle)
area = side1_rectangle*side2_rectangle

#виведемо результат
print('пеример={0}см.'.format(perimeter))
print('площа={0}см.'.format(area))