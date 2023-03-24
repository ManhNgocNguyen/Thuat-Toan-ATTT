def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def find_a_b(m, n, d):
    arr = []
    for i in range(m+1, n):
        for j in range(m+1, n):
            tmp = []
            if gcd(i, j) == d and i < j:
                tmp.append(i)
                tmp.append(j)
                arr.append(tmp)
    return arr


if __name__ == '__main__':
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    d = int(input("Nhập d: "))
    while m > 1000 or n > 1000 or d > 1000 or m < 0 or n < 0 or d < 0:
        print("Nhập lại!!! (0 < m, n, d < 1000)")
        m = int(input("Nhập m: "))
        n = int(input("Nhập m: "))
        d = int(input("Nhập m: "))

    arr = find_a_b(m,n,d)
    if len(arr) > 0:
        print(f'Các cặp số thỏa mãn là {arr}')
    else:
        print("Không có cặp số nào")
