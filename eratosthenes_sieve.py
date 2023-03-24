import math


def prime_eratosthenes(n):
    c = []
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    for i in range(2, n+1):
        if prime[i]:
            c.append(i)
    return c
