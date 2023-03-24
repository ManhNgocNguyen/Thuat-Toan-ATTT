import random
import math

def find_s_r(n):
    s = 1
    while True:
        if (n-1) % (2**s) != 0:
            break
        s += 1
    s = s-1
    r = (n-1)//(2**s)
    return s, r


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


def is_prime_rabin(n, t):
    s, r = find_s_r(n)
    for i in range(1, t):
        a = random.randint(2, n-2)
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


def getNum(k):
    k = '1' * k
    num = random.randint(0, int(k, 2))
    return num


def getPrimeNumber(k, t):
    num = getNum(k)
    while True:
        if is_prime_rabin(num, t):
            print(num)
            break
        else:
            num = getNum(k)



getPrimeNumber(10,10)
