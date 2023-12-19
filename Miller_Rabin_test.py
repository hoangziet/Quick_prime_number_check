import random
def binaryPower(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return binaryPower(a * a % n, b // 2, n)
    if b % 2 == 1:
        return a * binaryPower(a * a % n, b // 2, n) % n

def check_composite(n, a, d, s):
    x = binaryPower(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(1, s):
        x = binaryPower(x, 2, n)
        if x == n - 1:
            return False
    return True

def MillerRabin_test(n, iter=5):
    if n < 4:
        return n == 2 or n == 3
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(iter):
        rd = random.randint(2, n - 1)
        if check_composite(n, rd, d, s):
            return False
    return True

# print(MillerRabin_test(12))