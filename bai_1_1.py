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


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    s = int(input("Nhập kích thước mảng: "))
    arr = []
    p = 2147483647
    w = 8
    for i in range(s):
        element = int(input(f"Nhập giá trị arr[{i}]: "))
        arr.append(element)
    print(f'{n} -> {numb_to_arr(n, p, w)}')
    print(f'{arr} -> {arr_to_num(arr, p, w)}')
