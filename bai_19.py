import math


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def find_x(a, b, c, n, m):
    arr = []

    for i in range(n, m+1):
        if is_prime(a * (i ** 2) + b * i + c):
            arr.append(i)
    return arr


if __name__ == '__main__':
    a = int(input("Nhập a : "))
    b = int(input("Nhập b : "))
    c = int(input("Nhập c : "))
    n = int(input("Nhập n : "))
    m = int(input("Nhập m : "))
    while n >= m:
        print("Nhập lại!!!(n < m)")
        n = int(input("Nhập n : "))
        m = int(input("Nhập m : "))
    arr = find_x(a, b, c, n, m)
    if len(arr) > 0:
        print(f'x = {arr} ')
    else:
        print(f'Không có giá trị x nào nhỏ hơn {n} thỏa mãn')
