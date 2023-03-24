def multiple_and_square(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    bina = []
    for i in bin(k)[2::][::-1]:
        bina.append(i)
    if bina[0] == '1':
        b = a
    for i in range(1, len(bina)):
        if bina[i] == '0':
            A = pow(A, 2, n)
            continue
        if bina[i] == '1':
            A = pow(A, 2, n)
            b = (b * A) % n
    return b


if __name__ == '__main__':
    a = int(input("Nhập số a: "))
    k = int(input("Nhập số k: "))
    n = int(input("Nhập số n: "))
    print(f'{a}^{k} mod {n} = {multiple_and_square(a, k, n)}')

