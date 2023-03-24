import math


def prime_eratosthenes(n):
    c = []
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if prime[i]:
            for j in range(i**2, n+1, i):
                prime[j] = False
    for i in range(2, n+1):
        if prime[i]:
            c.append(i)
    return c


def prime_eratosthenes_segment(n, m):
    x = []
    start = 2
    while start <= n:
        end = start + m
        if end > n: # Trường hợp điểm kết thúc lớn hơn n
            end = n + 1
        arr = [i for i in range(start, end)]
        x.append(arr)
        start = end
    end = max(x[0])
    prime = prime_eratosthenes(end)
    for i in range(2, int((n-2+1)/m+1)):# Xét từ đoạn 2 trở đi
        tmp = x[i-1]
        c = [True]*(n - n//m - 2)
        m = math.floor(math.sqrt(max(tmp)))
        for p in range(2, m+1):
            if c[p]:
                for j in range(len(tmp)):
                    if tmp[j] % p == 0:
                        c[j] = False
        for k in range(0, len(tmp)):
            if c[k]:
                prime.append(tmp[k])
    return prime
