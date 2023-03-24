import math


def uoc(n):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
           arr.append(i)
    return arr


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def uoc_nguyen_to(arr):
    a = []
    for i in arr:
        if is_prime(i):
           a.append(i)
    return a

if __name__ == '__main__':
    n = int(input("Nhập n: "))
    print(f'Số ước của {n} là : {len(uoc(n))}')
    print(f'Số ước nguyên tố của {n} là : {len(uoc_nguyen_to(uoc(n)))}')
