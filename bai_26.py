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
    while n <=0:
        print("Nhập n nguyên dương")
        n = int(input("Nhập n: "))
    arr = array_prime(n)
    arr_mul = [i**2 for i in arr]
    num = []
    for i in range(n):
        for j in range(len(arr)):
            if i % arr_mul[j] == 0 and i % arr[j] == 0 and i > 0:
                num.append(i)
    if len(num) > 0:
        print(f"Các số S-num nhỏ hơn {n} là: {num}")
    else:
        print("Không có số nào thỏa mãn")