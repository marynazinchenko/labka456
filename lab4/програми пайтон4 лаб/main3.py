# Трикутник задається координатами своїх вершин на площині: . Визначити, чи є цей трикутник гострокутним.
# вводимо позначення
'''
 1 сторонa трикутника - side_a
 2 сторона трикутника - side_b
 3 сторона трикутника - side_c
координати трикутника - x1 x2 y1 y2 x3 y3
'''
#введення
import math

x1 = float(input('x1:'))
y1 =float(input('y1:'))
x2 = float(input('x2:'))
y2  = float(input('y2:'))
x3 = float(input('x3:'))
y3 = float(input('y3:'))

side_a = round(math.sqrt((x2-x1)**2 + (y2-y1)**2),0)
side_b = round(math.sqrt((x3-x2)**2 + (y3-y2)**2),0)
side_c = round(math.sqrt((x1-x3)**2 + (y1-y3)**2),0)


ab_corner = round(180 / math.pi * math.acos((side_b**2 +side_c**2 -side_a**2)/(2*side_b*side_c)))
bc_corner = round(180 / math.pi * math.acos((side_a**2 +side_c**2 -side_b**2)/(2*side_a*side_c)))
ac_corner = 180-ab_corner-bc_corner

print (ab_corner)
print (bc_corner)
print (ac_corner)


if ab_corner < 90 and bc_corner < 90 and ac_corner < 90:
    print("трикутник гострокутний")
else:
    print("трикутник не гострокутний")



