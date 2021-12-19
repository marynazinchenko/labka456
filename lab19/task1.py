#Дано текстовий файл, який містить дійсні числа. Яких елементів більше – додатних чи від’ємних.
import math
sum=0
d=0
a=open('file.txt')
e=a.readlines()
print(e)
for el in e:
    if el<'0':
        sum=1+sum
    else:
        if el>'0':
            d+=1
if sum>d:
    print('більше від\'ємних елементів')
else:
    print('більше додатніх елементів')
print(sum)
print(d)


