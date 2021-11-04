import numpy as np
a1= float(input('a1:'))
a2= float(input('a2:'))
a3= float(input('a3:'))
b1= float(input('b1:'))
b2= float(input('b2:'))
b3= float(input('b3:'))
x = np.array([a1,a2,a3])
y = np.array([b1,b2,b3])
product = a1*b1+a2*b2+a3*b3
print('скалярний добуток={0}'.format(product))


