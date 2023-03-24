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
        a = random.randint(2, n - 1)
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


def getNum():
    num = random.randint(0, 1000)
    return num


def getPrimeNumber():
    num = getNum()
    while True:
        if is_prime_rabin(num):
            return num
        else:
            num = getNum()


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
    n = int(input("Nhập n: "))
    p = getPrimeNumber()
    arr = []
    while n <= 0 or n >= 1000:
        print("Yêu cầu nhập 0 < n < 1000")
        n = int(input("Nhập n: "))
    while p >= 100 or p <= 0:
        p = getPrimeNumber()
    for i in range(n):
        result = multiple_and_square(i, p, n)
        if is_prime(result):
            arr.append(i)
    print(f'p = {p}')
    if len(arr) > 0:
        print(f'Các số a thỏa mãn a^{p} mod {n} là số nguyên tố =  {arr}')
    else:
        print("Không có số a thỏa mãn")

