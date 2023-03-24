def uc(n):
    flag = 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
            flag += 1
    return flag


def uc_4(n):
    arr = []
    for i in range(n+1):
        if uc(i) == 2: # Có sẵn 2 ước là 1 và chính nó rồi nên chọn 2 thôi
            arr.append(i)
    return arr

if __name__ == '__main__':
    n = int(input("Nhập n: "))
    arr = uc_4(n)
    if len(arr) > 0:
        print(f"Các số có 4 ước nguyên dương nhỏ hơn bằng {n} là : {arr} ")
    else:
        print(f"Không có số thỏa mãn")


