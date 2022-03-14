from queue import PriorityQueue
import math


def main():
    c = int(input())
    for case in range(c):
        input()
        n = int(input())
        q = PriorityQueue()
        hnit = []
        for i in range(n):
            (x, y) = tuple([float(x) for x in input().split()])
            for idx, h in enumerate(hnit):
                (x2, y2) = h
                d = math.sqrt(math.pow(x - x2, 2) + math.pow(y - y2, 2))
                q.put((d, (i, idx)))
            hnit.append((x, y))

        p = [-1 for i in range(n)]

        def find(x):
            if p[x] < 0:
                return x
            else:
                p[x] = find(p[x])
                return p[x]

        def join(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            if p[rx] > p[ry]:
                p[ry] += p[rx]
                p[rx] = ry
            else:
                p[rx] += p[ry]
                p[ry] = rx

        W = 0
        # leggir = []
        while -p[find(0)] != n:
            if q.empty():
                break
            (w, (u, v)) = q.get()
            if find(u) == find(v):
                continue
            # if u < v:
            # leggir.append((u, v))
            # else:
            # leggir.append((v, u))
            W += w
            join(u, v)

        if -p[find(0)] != n:
            print("Impossible")
        else:
            if case != 0:
                print()
            print("{:.2f}".format(W))
            # leggir.sort()
            # for leg in leggir:
            # (x, y) = leg
            # print(x, y, sep=" ")


if __name__ == "__main__":
    main()
