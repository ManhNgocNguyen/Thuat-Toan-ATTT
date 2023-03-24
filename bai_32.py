import random
import math


def find_s_r(n):
    s = 1
    while True:
        if (n - 1) % (2 ** s) != 0:
            break
        s += 1
    s = s - 1
    r = (n - 1) // (2 ** s)
    return s, r


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


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


def is_prime_rabin(n):
    s, r = find_s_r(n)
    for i in range(1, 10):
        a = random.randint(2, n - 2)
        y = multiple_and_square(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = multiple_and_square(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
        return True


def get_num():
    num = random.randint(10, 1000)
    return num


def get_prime_number():
    num = get_num()
    while True:
        if is_prime_rabin(num):
            return num
        else:
            num = get_num()


if __name__ == '__main__':
    sbd = int(input("Nhập số báo danh: "))
    p = get_prime_number()
    q = get_prime_number()
    while p < 100:
        p = get_prime_number()
    while q > 500 or p == q:
        q = get_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = pow(e,-1,phi)
    print(d)
    m = sbd + 123
    ct = multiple_and_square(m,e,n)
    pt = multiple_and_square(ct, d, n)
    print(f'Giá trị p = {p}')
    print(f'Giá trị q = {q}')
    print(f'Giá trị n = {n}')
    print(f'Giá trị e = {e}')
    print(f'Giá trị phi = {phi}')
    print(f'Giá trị mã hóa c = {ct}')
    print(f'Giải mã c ta thu được {pt}')
