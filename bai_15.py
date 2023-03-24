def eratosthenes(n):
    prime = []
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, n+1):
        if arr[i]:
            for j in range(i**2, n+1, i):
                arr[j] = False

    for i in range(len(arr)):
        if arr[i]:
            prime.append(i)

    return prime


if __name__ == '__main__':
    n = int(input("Nhập n : "))
    prime = eratosthenes(n)
    arr = []
    for i in prime:
        for j in prime:
            if j - i == 2 and i < j:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                arr.append(tmp)
    if len(arr) > 0:
        print(f"Cặp số nguyên tố sinh đôi nhỏ hơn bằng {n} là: {arr}")
    else:
        print("Không có cặp số nào thỏa mãn")

