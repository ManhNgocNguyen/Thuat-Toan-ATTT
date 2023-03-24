import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':

    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    while a <= 0 or b >= 1000:
        print("Nhập lại a,b (a>0, b <1000)")
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
    result = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            if i < j and is_prime(gcd(i, j)) and i != 0:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                result.append(tmp)
    if len(result) >0:
        print(f'Các cặp số có ước chung lớn nhất là số nguyên tố trong đoạn [{a}; {b}] là: {result}')
    else:
        print("Không có cặp số thỏa mãn")