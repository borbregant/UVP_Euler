def euler3(n):
    najvecji = 1
    p = 3
    while n != 1:
        while n % p == 0:
            najvecji = p
            n = n / p
        p += 2
    return najvecji