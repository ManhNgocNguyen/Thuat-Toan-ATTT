import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_x(a, b, c, n):
    arr = []

    for i in range(1, n):
        if is_prime(a * (i ** 2) + b * i + c):
            arr.append(i)
    return arr


if __name__ == '__main__':
    a = int(input("Nhập a : "))
    b = int(input("Nhập b : "))
    c = int(input("Nhập c : "))
    n = int(input("Nhập n : "))
    arr = find_x(a, b, c, n)
    if len(arr) > 0:
        print(f'x = {min(arr)} ')
    else:
        print(f'Không có giá trị x nào nhỏ hơn {n} thỏa mãn')
