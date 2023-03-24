import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


if __name__ == '__main__':
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    arr = []
    for i in range(a, b+1):
        if is_prime(i):
            arr.append(i)
    if is_prime(sum(arr)):
        print('Yes')
    else:
        print('No')
