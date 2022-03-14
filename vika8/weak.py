def main():
    n = int(input())
    while n != -1:
        grannar = []
        for i in range(n):
            rod = [int(x) for x in input().split()]
            granni = []
            for j in range(n):
                if rod[j] == 1:
                    granni.append(j)
            grannar.append(granni)

        d = [-1 for i in range(n)]
        weak = []

        for i in range(n):
            if d[i] != -1:
                continue
            s = grannar[i]
            for g in s:
                for r in grannar[g]:
                    if r in s and r != i and r != g:
                        d[r] = 0
                        d[g] = 0
                        d[i] = 0
            if d[i] == -1:
                d[i] = 1
                weak.append(i)
        weak.sort()
        print(*weak)

        n = int(input())


if __name__ == "__main__":
    main()
