import math


def prime_normal(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input("Nhập số cần kiểm tra: "))
    if prime_normal(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải số nguyên tố")
