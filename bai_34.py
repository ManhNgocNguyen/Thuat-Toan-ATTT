import random


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


def is_prime_fermat(n,t):
    base = []
    for i in range(1, t):
        a = random.randint(2, n - 2)
        base.append(a)
        r = multiple_and_square(a, n - 1, n)
        if r != 1:
            return False
    return True


def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def isCarmichael(n):
    if isPrime(n):
        return False
    elif n < 2:
        return False
    b = 2
    while (b < n):
        if gcd(b, n) == 1:
            if pow(b, n - 1, n) != 1:
                return False
        b += 1
    return True


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    t = int(input("Nhập t: "))
    if is_prime_fermat(n,t):
        print(f'{n} là số nguyên tố')
    else:
        print(f'{n} là không số nguyên tố')

