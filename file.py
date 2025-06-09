set1 = 2
set2 = 3
set3 = 5
set4 = 7

iterations = 30

size_tple = (set1, set2, set3)

def productN(n):
    result = 1
    for num in size_tple[: len(size_tple) + 1 - n]: 
        result *= num
    return result

def itaResidue(n):
    if n == 1: return iterations
    return itaResidue(n - 1) - ((itaResidue(n - 1) - 1)//productN(n - 1))*productN(n - 1)

def itaQuantity(n):
    return ((itaResidue(n) - 1)//productN(n)) + 1

print([itaResidue(k) for k in range(1, 5)])
print([itaQuantity(k) for k in range(1, 5)])
print([(itaQuantity(k) - 1)*productN(k) for k in range(1, 4)] , itaQuantity(4))

