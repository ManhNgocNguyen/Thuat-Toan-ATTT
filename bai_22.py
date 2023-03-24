import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def caculate(n):
    if is_prime(n):
        n = n
    else:
        n = 0
    return n


def f_i_j(l, r):
    sum = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if j > i:
                sum += caculate(j) * caculate(i)

    return sum


if __name__ == '__main__':
    l = int(input("Nhập L: "))
    r = int(input("Nhập R: "))
    print(f_i_j(l, r))
