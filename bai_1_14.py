import random


def find_s_r(n):
    s = 1
    while True:
        if (n - 1) % (2 ** s) != 0:
            break
        s += 1
    s = s - 1
    r = (n - 1) // (2 ** s)
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
        A = pow(A, 2, n)
        if bina[i] == '1':
            b = (b * A) % n
    return b


def is_prime_rabin(n, t):
    s, r = find_s_r(n)
    for i in range(t):
        a = random.randint(2,n-1)
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


if __name__ == '__main__':
    n = int(input("Nhập số n: "))
    t = int(input("Nhập số lần kiểm tra: "))
    if is_prime_rabin(n, t):
        print(f'{n} là số nguyên tố ')
    else:
        print(f'{n} không phải số nguyên tố')
