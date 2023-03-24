import math 


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

  
def pollard_rho(n):
    a = 2
    b = 2
    arr = []
    while True:
        a = (a**2 + 1) % n
        b = (b**2 + 1) % n
        b = (b**2 + 1) % n
        d = gcd(abs(a-b), n)
        arr.append(d)
        if 1 < d < n:
            return f"Thừa số không tầm thường của {n} = {d}"
        elif d == n:
            return f"{n} không có thừa số không tầm thường"
