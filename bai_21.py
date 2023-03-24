import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_super_prime(n):
    flag = 0
    for i in range(1, n):
        if is_prime(i):
            flag += 1
    if is_prime(flag):
        return True
    else:
        return False


if __name__ == '__main__':
    a = int(input("Nhập a: "))
    b = int(input("Nhap b: "))
    arr = []
    for i in range(a, b+1):
        if is_super_prime(i):
            arr.append(i)
    print(f'[{a}, {b}] có {len(arr)}  số siêu nguyên tố')
