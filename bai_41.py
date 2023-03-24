def multiple_and_square(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    bina = []
    for i in bin(k)[2::][::-1]:
        bina.append(i)
    if bina[0] == '1':
        b = a
    for i in range(1, len(bina)):
        if bina[i] == '0':
            A = pow(A, 2, n)
            continue
        if bina[i] == '1':
            A = pow(A, 2, n)
            b = (b * A) % n
    return b

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    a = int(input("Nhập a: "))
    k = int(input("Nhập k: "))
    n = int(input("Nhập n: "))
    while a > 1000 or k > 1000 or n > 1000 or a < 0 or k < 0 or n < 0:
        print("Yêu cầu 0 < a, k, n < 1000")
        a = int(input("Nhập a: "))
        k = int(input("Nhập k: "))
        n = int(input("Nhập n: "))
    result = multiple_and_square(a, k, n)
    if is_prime(result):
        print(f"{a}^{k} mod {n} = {result} là số nguyên tố")
    else:
        print(f"{a}^{k} mod {n} = {result} không là số nguyên tố")
