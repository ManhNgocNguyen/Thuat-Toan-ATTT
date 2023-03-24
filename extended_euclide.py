def ex_gcd(a, b):
    m, n = a, b
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    while n != 0:
        q = m // n
        r = m % n
        x, y = x1 - q * x2, y1 - q * y2
        m = n
        x1, y1 = x2, y2
        n = r
        x2, y2 = x, y
        if a * x1 + b * y1 == 1:
            return f"d = {1}, a^-1 mod b = {x1+b}, b^-1 mod a = {y1}"
    return f"gcd{a, b} = {a*x1 + b * y1}"
