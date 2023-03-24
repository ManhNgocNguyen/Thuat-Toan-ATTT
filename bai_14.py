def eratosthenes():
    a = 100
    b = 999
    prime = []
    arr = [True] * (b+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, b+1):
        if arr[i]:
            for j in range(i**2, b+1, i):
                arr[j] = False

    for i in range(len(arr)):
        if arr[i] and i >= a:
            prime.append(i)

    return prime


def reversed(num):
    reversed_num = 0
    while num !=0:
        digit = num %10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num


if __name__ == '__main__':
    prime = eratosthenes()
    for i in prime:
        if pow(reversed(i), 1/3) == int(pow(reversed(i), 1/3)):
            print(i)
