import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def pollard_rho(n, c):
    a, b = 2, 2
    if (c == 10): return -1
    while (True):
        a = (a ** 2 + c) % n
        b = (b ** 2 + c) % n
        b = (b ** 2 + c) % n
        d = gcd(abs(a - b), n)
        if 1 < d < n:
            return d
        if d == n:
            return pollard_rho(n, c + 1)


if __name__ == '__main__':
    n = int(input("Nhập số n:"))
    result = (pollard_rho(n, 1))
    if result == -1:
        print(f"{n} không có thừa số không tầm thường")
    else:
        print(f"Thừa số không tầm thường của {n} = {result}")
