import math
import random


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10*n))
    return arr


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    prime = []
    n = int(input("Nhập kích thước mảng n : "))
    arr = generate_array(n)
    print(f'Mảng sinh ngẫu nhiên là: {arr}')
    for i in arr:
        if is_prime(i):
            prime.append(i)
    print(f'Các số nguyên tố là: {prime}')


