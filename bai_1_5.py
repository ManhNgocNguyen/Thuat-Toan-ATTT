import math


def arr_to_num(array, p, w):
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    a = 0
    for i in array:
        a += i * pow(2, w * (t - 1))
        t -= 1
    return a


def numb_to_arr(a, p, w):
    array = []
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    while t >= 1:
        arr = a // pow(2, w * (t - 1))
        a = a % pow(2, w * (t - 1))
        array.append(arr)
        if t == 1:
            return array
        t -= 1


def minus(a, b, p, w):
    c = []
    e = [0, 1]
    epsilon = 0
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    index = 0
    for i in range(len(a)):
        arr = a[i] - b[i] - e[index]
        if arr < 0:
            index = 1
        else:
            index = 0
        if a[len(a) - 1] - b[len(a) - 1] - e[index] < 0:
            epsilon = 1
        else:
            epsilon = 0
        c.append(arr % pow(2, w))
    return epsilon, c[::-1]


def sum(a, b, p, w):
    c = []
    e = [0, 1]
    epsilon = 0
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    index = 0
    for i in range(len(a)):
        arr = a[i] + b[i] + e[index]
        if arr >= pow(2, w):
            index = 1
        else:
            index = 0
        if a[len(a) - 1] + b[len(a) - 1] + e[index] >= pow(2, w):
            epsilon = 1
        else:
            epsilon = 0
        c.append(arr % pow(2, w))
    return epsilon, c[::-1]


def minus_fp(a, b, p, w):
    e, c = minus(a, b, p, w)
    if e == 1:
        e, c = sum(arr_to_num(c, p, w), p, p, w)
    return c


if __name__ == '__main__':
    w = 8
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    p = int(input("Nhập số p: "))
    print(f'{a} - {b} =  {minus(a, b, p, w)}')
    print(f'{a} - {b} (fp) = {minus_fp(a, b, p, w)} ')
    print(f'{a} - {b} (fp) = {arr_to_num(minus_fp(a, b, p, w),p,w)} ')

