def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**1/2)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    arr = []
    n = int(input("Nhập kích thước mảng: "))
    for i in range(n):
        element = int(input(f'Giá trị arr[{i}] = '))
        while element < 1:
            print("Yêu cầu giá trị nguyên dương")
            element = int(input(f'Nhập lại giá trị arr[{i}] = '))
        arr.append(element)
    result = []
    for i in arr:
        for j in arr:
            if is_prime(gcd(i, j)) and i < j:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                result.append(tmp)
    if len(result) >0:
        print(f'Cặp số có ước chung lớn nhất là số nguyên tố là: {result}')
    else:
        print(f'Không có cặp số thỏa mãn')
