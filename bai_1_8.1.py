def ex_gcd_fp(a, b):
    u = a
    v = b
    x1 = 1
    x2 = 0
    while u != 1:
        q = v // u
        r = v % u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return f"{a}^-1 mod {b} = {x1 % b}"


if __name__ == '__main__':
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    while a < 0 or b < 0:
        print("Nhập a,b > 0")
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
    print(ex_gcd_fp(a, b))


    
