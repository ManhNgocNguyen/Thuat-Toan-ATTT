import math


def eratosthenes(a, b):
    if b < 0 and a < 0:
        return 0
    if a < 0:
        a = 0
    flag = 0
    arr = [True] * (b + 1)
    arr[0] = False
    arr[1] = False
    for i in range(2, b + 1):
        if arr[i]:
            for j in range(i ** 2, b + 1, i):
                arr[j] = False

    for i in range(len(arr)):
        if arr[i] and i >= a:
            flag += 1

    return flag


if __name__ == '__main__':
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    while a >= b:
        print("Nhập a < b")
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
    print(f"Số nguyên tố nằm trong [{a},{b}] = {eratosthenes(a, b)}")
