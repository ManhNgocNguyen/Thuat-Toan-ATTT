import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum = i
    return sum


def check(x, s1, s2):
    for i in s1:
        for j in s2:
            if x == i + j:
                return True
    return False


if __name__ == '__main__':
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    while a > b:
        print("Nhập lại A, B (A < B)")
        a = int(input("Nhập A: "))
        b = int(input("Nhập B: "))
    s1 = [i**2 for i in range(1, b+1)]
    s2 = [i**2 for i in range(1, b+1)]
    flag = 0
    arr = []
    for i in range(a, b+1):
        if is_prime(i) and check(i, s1, s2):
            flag += 1
            arr.append(i)
    print(f"Số lượng số nguyên tố thỏa mãn là {flag} ")
    print(f"Các số đó là {arr}")
