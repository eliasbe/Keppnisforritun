from math import ceil, sqrt


def square_digits(x):
    summa = 0
    while x:
        eining = x % 10
        summa += eining * eining
        x = int(x / 10)
    return summa


def happy(x):
    sett = set()
    while True:
        x = square_digits(x)
        if x == 1:
            return True
        if x in sett:
            return False
        sett.add(x)


def isprime(n):
    sqrtn = ceil(sqrt(n))
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, sqrtn, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


def main():
    p = int(input())
    for i in range(p):
        (k, m) = tuple([int(x) for x in input().split()])
        if happy(m) and isprime(m):
            answer = "Yes"
        else:
            answer = "No"
        print(k, m, answer, sep=" ")


if __name__ == "__main__":
    main()
