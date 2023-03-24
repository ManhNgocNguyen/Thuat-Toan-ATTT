import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def array_prime(n):
    arr = []
    for i in range(0, n+1):
        if is_prime(i):
            arr.append(i)
    return arr


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    while n > 10000 or n <1:
        print("1 <= n <= 10000")
        n = int(input("Nhập lại n: "))
    arr = array_prime(n)
    result = []
    for i in arr:
        for j in arr:
            for k in arr:
                if i < j < k and n == i + j +k:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j)
                    tmp.append(k)
                    result.append(tmp)
    if len(result) >0:
        print(f"Các cặp số thỏa mãn là {result}")
    else:
        print("Không có cặp số thỏa mãn")
