import math
import random


def numb_to_arr(a, p, w):
    array = []
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    while t >= 1:
        arr = a // pow(2, w * (t - 1))
        a = a % pow(2, w * (t - 1))
        array.append(arr)
        if t == 1:
            return array
        t -= 1


def arr_to_num(array, p, w):
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    a = 0
    for i in array:
        a += i * pow(2, w * (t - 1))
        t -= 1
    return a


def sum(a, b, p, w):
    c = []
    e = [0, 1]
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    index = 0
    for i in range(len(a)):
        arr = a[i] + b[i] + e[index]
        if arr >= pow(2, w):
            index = 1
        else:
            index = 0
        if a[len(a) - 1] + b[len(a) - 1] + e[index] >= pow(2, w):
            epsilon = 1
        else:
            epsilon = 0
        c.append(arr % pow(2, w))
    return epsilon, c[::-1]


def minus(a, b, p, w):
    c = []
    e = [0, 1]
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    index = 0
    for i in range(len(a)):
        arr = a[i] - b[i] - e[index]
        if arr >= pow(2, w) or arr < 0:
            index = 1
        else:
            index = 0
        if a[len(a) - 1] - b[len(a) - 1] - e[index] < 0 or a[len(a) - 1] - b[len(a) - 1] - e[index] < 0:
            epsilon = 1
        else:
            epsilon = 0
        c.append(arr % pow(2, w))
    return epsilon, c[::-1]


def sum_fp(p, a, b, w):
    old_e, old_c = sum(a, b, p, w)
    if old_e == 1:
        new_e, new_c = minus(arr_to_num(old_c, p, w), p, p, w)
        return new_e, new_c
    else:
        return old_e, old_c


def minus_fp(p, a, b, w):
    old_e, old_c = minus(a, b, p, w)
    if old_e == 1:
        new_e, new_c = sum(arr_to_num(old_c, p, w), p, p, w)
        return new_e, new_c
    else:
        return old_e, old_c


def multiple(p, a, b, w):
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    c = [0] * 2 * t  # Khởi tạo mảng bằng 2 lần t vì tí còn add 2w bit vào mảng

    def convert_uv_to_u_v(uv):
        bin_uv = str(bin(uv)[2:])
        if len(bin_uv) < 16:
            bin_uv = "0" * (16 - len(bin_uv)) + bin_uv  # Trường hợp không đủ 16 bit thì chèn thêm các bit 0 vào trước
        u = int(bin_uv[:8], 2)
        v = int(bin_uv[8:], 2)
        return u, v

    for i in range(t):
        u = 0
        for j in range(t):
            uv = c[i + j] + a[i] * b[j] + u
            u, v = convert_uv_to_u_v(uv)
            c[i + j] = v
        c[i + t] = u
    return c[::-1]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ex_gcd(a, b):
    m, n = a, b
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    while n != 0:
        q = m // n
        r = m % n
        x, y = x1 - q * x2, y1 - q * y2
        m = n
        x1, y1 = x2, y2
        n = r
        x2, y2 = x, y
        if a * x1 + b * y1 == 1:
            return f"d = {1}, a^-1 mod b = {x1 + b}, b^-1 mod a = {y1}"
    return f"gcd{a, b} = {a * x1 + b * y1}"


def ex_gcd_fp(a, b):
    u = a
    v = b
    x1 = 1
    x2 = 0
    while u != 1:
        q = v // u
        r = v % u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return f"{a}^-1 mod {b} = {x1 % b}"


def find_prime_normal(n):
    c = []

    def is_prime(m):
        if m < 2:
            return False
        for i in range(2, int(math.sqrt(m)) + 1):
            if m % i == 0:
                return False
        return True

    for i in range(2, n + 1):
        if is_prime(i):
            c.append(i)
    return c


def prime_eratosthenes(n):
    c = []
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if prime[i]:
            for j in range(i ** 2, n + 1, i):
                prime[j] = False
    for i in range(2, n + 1):
        if prime[i]:
            c.append(i)
    return c


def prime_eratosthenes_segment(n, m):
    x = []
    start = 2
    while start <= n:
        end = start + m
        if end > n:  # Trường hợp điểm kết thúc lớn hơn n
            end = n + 1
        arr = [i for i in range(start, end)]
        x.append(arr)
        start = end
    end = max(x[0])
    prime = prime_eratosthenes(end)
    for i in range(2, int((n - 2 + 1) / m + 1)):  # Xét từ đoạn 2 trở đi
        tmp = x[i - 1]
        c = [True] * (n - n // m - 2)
        m = math.floor(math.sqrt(max(tmp)))
        for p in range(2, m + 1):
            if c[p]:
                for j in range(len(tmp)):
                    if tmp[j] % p == 0:
                        c[j] = False
        for k in range(0, len(tmp)):
            if c[k]:
                prime.append(tmp[k])
    return prime


def find_thua_so(n):
    c = []
    i = 2
    while True:
        r = n % i
        if r == 0:
            n = n / i
            c.append(i)
            if n == 1:
                break
        else:
            i += 1
    return c


def is_prime(m):
    if m < 2:
        return False
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True


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


def is_prime_fermat(n):
    base = []
    for i in range(1, 10):
        a = random.randint(2, n - 2)
        base.append(a)
        r = multiple_and_square(a, n - 1, n)
        if r != 1:
            return f"{n} là hợp số"
    return f"{n} là số nguyên tố của cơ sở {base}"


def prime_normal(n):
    c = []
    for i in range(n):
        if is_prime(i):
            c.append(i)
    return c


def pollard_rho(n):
    a = 2
    b = 2
    arr = []
    while True:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        d = gcd(abs(a - b), n)
        arr.append(d)
        if 1 < d < n:
            return f"Thừa số không tầm thường của {n} = {d}"
        elif d == n:
            return f"{n} không có thừa số không tầm thường"



