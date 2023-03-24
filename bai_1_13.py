
import random

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
        A = pow(A, 2, n)
        if bina[i] == '1':
            b = (b * A) % n
    return b


def is_prime_fermat(n,t):
    for i in range(t):
        a = random.randint(2,n-1)
        r = multiple_and_square(a, n - 1, n)
        if r != 1:
            return f"{n} là hợp số"
        return f"{n} là số nguyên tố "


if __name__ == '__main__':
    n = int(input("Nhập số n: "))
    t = int(input("Nhap t : "))
    # a = int(input("Nhập cơ sở a: "))
    print(is_prime_fermat(n,t))

