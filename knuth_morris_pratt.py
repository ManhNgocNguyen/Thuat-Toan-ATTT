
def prefix(p):
    arr = []
    for i in range(len(p)):
        arr.append(p[0:i+1])
    return arr


def suffix(p):
    arr = []
    for i in range(len(p)):
        arr.append(p[i:len(p)])
    return arr


def failure_function(p):
    f = dict()
    flag = 0
    for i in range(len(p)):
        if i == 0:
            f[i] = -1
        else:
            pre = prefix(p[0:i])
            suf = suffix(p[1:i])
            suf_inv = suf[::-1]
            for (j, k) in zip(pre, suf_inv):
                if j == k:
                    flag += 1
            f[i] = flag
            flag = 0
    return f


def knuth_morris_pratt(p, t):
    i = 0
    j = 0
    m = len(p)
    n = len(t)
    f = failure_function(p)
    while i < n:
        while t[i] == p[j]:
            if j == m-1:
                print(f"Tìm {p} trong {t} ở vị trí {i-j}")
                break
            elif i == n-1:
                break
            else:
                i += 1
                j += 1

        i = i + j - f[j]
        j = f[j]
        if j == -1:
            j = 0


if __name__ == '__main__':
    t = input("Nhập chuỗi: ")
    p = input("Nhập chuỗi cần tìm: ")
    knuth_morris_pratt(p, t)
