def vsota_kvadratov(n):
    vsota = 0
    for i in range(n + 1):
        vsota += i ** 2
    return vsota

def kvadrat_vsote(n):
    vsota = 0
    for i in range(n + 1):
        vsota += i
    return vsota ** 2

print(vsota_kvadratov(100) - kvadrat_vsote(100))
