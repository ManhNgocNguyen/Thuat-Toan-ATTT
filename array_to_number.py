def arr_to_num(array, p, w):
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    a = 0
    for i in array:
        a += i * pow(2, w * (t - 1))
        t -= 1
    return a
