import random


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
