import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sum(arr):
    sum  = 0
    for i in arr:
        sum += i
    return sum


def loc_va_chia_thanh_k_so_lien_tiep(n, k):
    prime = []
    prime_k = []
    flag = 0
    p_k = []
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        for j in range(i**2, n+1, i):
            arr[j] = False

    for i in range(n+1): # Lấy mảng số nguyên tố nhỏ hơn bằng n
        if arr[i]:
            prime.append(i)
    i = 0
    while i < len(prime): # Lấy từng phần tử trong mảng nguyên tố rồi add vào mảng nguyên tố tạm thời và đánh dấu nếu đến
                         # k lần thì dừng lại và lại đưa mảng nguyên tố tạm thời và điểm đánh dấu về 0 và bắt đầu vòng lặp mới
        prime_k.append(prime[i])
        flag += 1
        if flag == k:
            p_k.append(prime_k)
            prime_k = []
            i -= k-1
            flag = 0
        i += 1
    return p_k


if __name__ == '__main__':
    arr = []
    n = int(input("Nhập n: "))
    while True:
        k = int(input("Nhập k : "))
        if k % 2 != 0:
            break
        else:
            print("K là số lẻ !! Nhập lại")
# notice: Với trường hợp k =4 thì chỉ có duy nhất 1 trường hợp là 2,3,5,7 vì nếu cả 4 là nguyên tố thì phải có số là số
# chẵn vì nếu cả 4 là số lẻ thì tổng lại là số chẵn nên không thể là số nguyên tố
    prime_n_k = loc_va_chia_thanh_k_so_lien_tiep(n, k)
    for i in prime_n_k:
        if is_prime(sum(i)) and sum(i) <= n:
            arr.append(i)

    if len(arr) > 0:
        print(f'{k} số nguyên tố liên tiếp là: {arr}')
    else:
        print(f'Không có {k} số nguyên tố liên tiếp thỏa mãn')



