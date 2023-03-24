import math


def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def uoc(n):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
           arr.append(i)
    return arr


def is_prime(n):
    if n == 1:
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
    s = len(uoc(n))
    p = sum(uoc(n))
    k = len(uoc_nguyen_to(uoc(n)))
    q = sum(uoc_nguyen_to(uoc(n)))
    print(f"Số ước của {n} là : s =  {s}")
    print(f"Tổng của các ước của {n} là: p = {p}")
    print(f"Số ước nguyên tố của {n} là: k = {k}")
    print(f"Tổng của các ước nguyên tố của {n} là: q = {q}")
    print(f"N+p+s-q-k = {n} + {p} + {s} - {q} - {k} = {n+p+s-q-k}")
