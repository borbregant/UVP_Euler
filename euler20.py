import math

def vsota_stevk(n):
    if n > 0:
        return n % 10 + vsota_stevk(n // 10)
    else:
        return 0

print(vsota_stevk(math.factorial(100)))
