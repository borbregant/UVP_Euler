def palindrom(niz):
    return niz == niz[::-1]

i = 100
j = 100
najvecji = 0
while (i <= 999):
    while (j <= 999):
        produkt = i * j
        if (produkt > najvecji and palindrom(str(produkt))):
            najvecji = produkt
        j += 1
    j = 100
    i += 1
print(najvecji)

