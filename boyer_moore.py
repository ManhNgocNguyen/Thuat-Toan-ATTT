import string


def last_occurrence(p):
    l = dict()
    a = string.ascii_letters + ' '
    for i in a:
        l[i] = p.rfind(i)
    return l


def boyer_moore(p, t):
    lx = last_occurrence(p)
    m = len(p)
    n = len(t)
    i = m - 1
    j = m - 1
    while i < n:
        if p[j] == t[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, 1 + lx[t[i]])
            j = m - 1

    return -1


if __name__ == '__main__':
    t = input("Nhập chuỗi: ")
    p = input("Nhập chuỗi cần tìm: ")
    result = boyer_moore(p, t)
    if result == -1:
        print(f'Không có {p} trong {t}')
    else:
        print(f'Chuỗi {p} xuất hiện trong {t} ở vị trí {result}')
