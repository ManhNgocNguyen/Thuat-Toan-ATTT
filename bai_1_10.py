import math
def is_normal_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


def find_normal_prime(n):
    arr = []
    for i in range(n+1):
        if is_normal_prime(i):
           arr.append(i)
    return arr


def prime_eratosthenes(n):
    c = [True] * (n+1)
    c[0] = False
    c[1] = False
    for i in range(2, n-1):
        for j in range(i**2, n+1, i):
            if c[i]:
                c[j] = False

    arr = []
    for i in range(len(c)):
        if c[i]:
            arr.append(i)
    return arr


def prime_eratosthenes_segment(n, m):
    x = []
    start = 2
    while start <= n:
        end = start + m
        if end > n: # Trường hợp điểm kết thúc lớn hơn n thì mình sẽ cộng thêm 1 vào để đủ đoạn
            end = n + 1
        arr = [i for i in range(start, end)]
        x.append(arr)
        start = end

    #Xét đoạn 1
    start = 2 # Vì số nguyên tố bắt đầu từ 2 nên em lấy điểm bắt đầu là 2
    end = start + m
    if end > n:
        end = n + 1
    arr = {} #Dùng hàm erothenes bình thường để tính số nguyên tố đoạn 1
    for i in range(start, end):
        arr[i] = True
    for i in range(start, end):
        if arr[i]:
            for j in range(i ** 2, end, i):
                arr[j] = False


    for i in range(2, math.ceil((n - 2 + 1) / m) + 1): #Tính số đoạn của của dãy số và bắt đầu xét từ đoạn thứ 2
        M = math.floor(math.sqrt(max(x[i - 1]))) # Tìm m là căn của phần tử lớn nhất trong đoạn làm tròn lên
        for j in x[i - 1]: # Gắn phần tử trong mảng là True
            arr[j] = True
        for p in [k for k in range(2, M + 1) if arr[k]]: # lấy các phần tử là số nguyên tố ở phần trước
            for j in x[i - 1]: # Rồi đem các phần tử ở đoạn này chia với các số nguyên tố đó nếu mà chia hết thì mình loại không thì giữ
                if j % p == 0: arr[j] = False

    primes = [i for i in range(2, n + 1) if arr[i]]
    return primes

if __name__ == '__main__':
    n = int(input("Nhập số n: "))
    m = int(input("Nhập kích cỡ của 1 đoạn m: "))
    print("Cách thông thường: ")
    print(find_normal_prime(n))
    print("Sàng eratosthenes: ")
    print(prime_eratosthenes(n))
    print("Sàng eratosthenes phân đoạn: ")
    print(prime_eratosthenes_segment(n, m))
