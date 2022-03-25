# from math import ceil, sqrt


def eratosthenes(maxn):
    # mxsq = ceil(sqrt(maxn))
    fylki = [0 for i in range(maxn)]
    for i in range(2, maxn):
        if fylki[i] == 0 and i < maxn // 2 + 1:  # and i <= mxsq:
            for j in range(i, maxn, i):
                k = j
                while k % i == 0:
                    fylki[j] += 1
                    k //= i
        if fylki[i] == 0:
            fylki[i] = 1
    return fylki


def main():
    f = eratosthenes(1000001)
    li = [0]
    for i in f:
        li.append(li[-1] + i)
    while True:
        try:
            n = int(input())
        except:
            break
        print(li[n + 1])


if __name__ == "__main__":
    main()
