
def find_by_vet_can(p, t):
    m = len(t)
    n = len(p)
    arr = []
    for i in range(m):
        if i + n > m:
            t = t + (i + n - m)*' ' # Chèn thêm dấu cách nếu chuỗi thiếu
        arr.append(t[i:i+n]) # tách chuỗi theo độ dài p
    for i in range(len(arr)):
        if p == arr[i]:
            return f'Đã tìm thấy chuỗi {p} ở vị trí {i} sau {i+1} lần', arr
        elif i > len(arr):
            return f'Không tìm thấy chuỗi {p} trong {t}'


if __name__ == '__main__':
    t = input("Nhập chuỗi: ")
    p = input("Nhập chuỗi cần tìm: ")
    print(find_by_vet_can(p, t))
