def ex_gcd(a, b):
    if b == 0:
        d = a
        x = 1
        y = 0
        return d, x, y
    x1 = 0
    y1 = 1
    x2 = 1
    y2 = 0
    while b > 0:
        q = int(a / b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2
    y = y2
    return d, x, y


if __name__ == '__main__':
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    while a < 0 or b < 0:
        print("Nhập a,b > 0")
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
    d, h, k = ex_gcd(a, b)
    if d == 1:
        print(f'gcd({a}, {b}) = {d}')
        print(f'{a}^-1 mod {b} = {h}')
        print(f'{b}^-1 mod {a} = {k}')
    else:
        print(f'gcd({a}, {b}) = {d}')
