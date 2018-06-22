def je_prastevilo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prastevilo(n):
    x=[]
    j=1
    while len(x)<n:
        if (je_prastevilo(j)) == True:
            x.append(j)
        j += 2
    return x[n-2]

print(prastevilo(10001))