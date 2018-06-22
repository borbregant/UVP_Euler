#a2 + b2 = c2

#a + b + c = 1000

def trojcek(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False

for a in range(1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a + b + c == 1000:
                if trojcek(a, b, c):
                    print(a * b * c)




