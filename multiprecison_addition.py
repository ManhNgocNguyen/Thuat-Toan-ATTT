import math


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
        
        
def sum(a, b, p, w):
    c = []
    e = [0, 1]
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    index = 0
    for i in range(len(a)):
        arr = a[i] + b[i] + e[index]
        if arr >= pow(2, w):
            index = 1
        else:
            index = 0
        if a[len(a)-1] + b[len(a)-1] + e[index] >= pow(2, w):
            epsilon = 1
        else:
            epsilon = 0
        c.append(arr % pow(2, w))
    return epsilon, c[::-1]
