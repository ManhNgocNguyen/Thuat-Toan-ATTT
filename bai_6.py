import math

def tong_uoc(n):
    sum = 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
           sum += i
    return sum + 1
def f_number(n):
    if n == tong_uoc(n):
        return True
    return False

if __name__ == '__main__':
    n = int(input("Nhập n: "))
    arr = []
    for i in range(2, n+1):
        if f_number(i):
            arr.append(i)
    if len(arr) > 0:
        print(f"Các số f_Number nhỏ hơn {n} là: {arr}")
    else:
        print("Không có số f_Number")
