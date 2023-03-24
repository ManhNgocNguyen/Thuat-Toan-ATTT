def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    while a <= 0 or b <= 0:
        print("Nhập a,b > 0")
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
    print(f'gcd({a}, {b}) = {gcd(a, b)}')
