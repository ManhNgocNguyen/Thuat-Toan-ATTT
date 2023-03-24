def find_by_vet_can(p, t):
    m = len(t)
    n = len(p)
    arr = []
    for i in range(0, m - n + 1):
        if p == t[i:i + n]:
            arr.append(f'Đã tìm thấy chuỗi {p} ở vị trí {i}')
    return arr


if __name__ == '__main__':
    t = input("Nhập chuỗi: ")
    p = input("Nhập chuỗi cần tìm: ")
    arr = find_by_vet_can(p, t)
    if len(arr) > 0:
        for i in arr:
            print(i)
    else:
        print(f'Không tìm thấy chuỗi {p}')

