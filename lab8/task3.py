#нехай х0=1 хі=хі-1+2і де і=1,2... Визначити х10

def fact(i):
    if i==0:
        return 1
    return fact(i-1)+2*i
print(fact(10))


