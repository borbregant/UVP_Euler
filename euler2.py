a = 0
b = 1
vsota = 0
while b <= 4000000:
    if b % 2 == 0:
        vsota += b
    a, b = b, a + b
print(vsota)
