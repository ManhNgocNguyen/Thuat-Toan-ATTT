import math


def eratosthenes(n):
    sum = 0
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(i**2, n+1, i):
            arr[j] = False

    for i in range(n + 1):
        if arr[i]:
            sum += i
    return sum

if __name__ == '__main__':
    n = int(input("Nhập n: "))
    print(f'Tổng các số nguyên tố nhỏ hơn bằng {n} là : {eratosthenes(n)}')

