import math


def eratosthenes(n):
    p = []
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    for i in range(n + 1):
        if arr[i]:
            for j in range(i ** 2, n + 1, i):
                arr[j] = False

    for i in range(n + 1):
        if arr[i]:
            p.append(i)

    return p


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def reversed(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


if __name__ == '__main__':
    arr = []
    n = int(input("Nhập n: "))
    prime_arr = eratosthenes(n)
    for i in prime_arr:
        if is_prime(reversed(i)):
            arr.append(i)

    if len(arr) > 0:
        print(f"Các số emirp nhỏ hơn bằng {n} là : {arr}")
    else:
        print("Không có số emirp")
