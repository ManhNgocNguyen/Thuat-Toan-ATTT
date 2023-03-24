import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def loc_va_chia_thanh_k_so_lien_tiep(n):
    prime = []
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(i**2, n+1, i):
            arr[j] = False

    for i in range(n+1): # Lấy mảng số nguyên tố nhỏ hơn n
        if arr[i]:
            prime.append(i)
    return prime


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    prime = loc_va_chia_thanh_k_so_lien_tiep(n)
    print(f"Cặp số nguyên tố nhỏ hơn {n} có tổng là 1 số nguyên tố là: ")
    for i in prime:
        for j in prime:
            if is_prime(i+j) and is_prime(abs(i-j)) and i < j:
                print(i,j)
# notice: tích và chia không có số nào vì nếu xảy ra thì số đó không còn là sô nguyên tố nữa
