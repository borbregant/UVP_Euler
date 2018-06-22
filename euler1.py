def euler1(n):
    vsota = 0
    for stevilo in range(n):
        if stevilo % 3 == 0 or stevilo % 5 == 0:
            vsota += stevilo
    return vsota