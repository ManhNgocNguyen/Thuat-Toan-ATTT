import math


def erathones_prime(n):
    prime = []
    tmp = n
    n = pow(10, int(n))
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(i**2, n+1, i):
                arr[j] = False
    for i in range(len(arr)):
        if arr[i]:
            if len(str(i)) == tmp:
                prime.append(i)
    return prime


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    print(f"Các số có nguyên tố có {n} chữ số là : {erathones_prime(n)}")
