from math import floor, sqrt


def perf(n):
    sqrtn = floor(sqrt(n))
    summa = 0
    for i in range(2, sqrtn + 1):
        if n % i == 0:
            summa += i + n / i
    if sqrtn == sqrt(n):
        summa -= sqrtn
    summa += 1
    return summa


def main():
    while True:
        try:
            n = int(input())
        except:
            break
        s = perf(n)
        if s == n:
            result = "perfect"
        elif abs(s - n) <= 2:
            result = "almost perfect"
        else:
            result = "not perfect"
        print(n, result, sep=" ")


if __name__ == "__main__":
    main()
