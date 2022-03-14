from queue import PriorityQueue


def main():
    (n, m) = tuple([int(x) for x in input().split()])
    while not (n == 0 and m == 0):
        q = PriorityQueue()
        for i in range(m):
            (u, v, w) = tuple([int(x) for x in input().split()])
            q.put((w, (u, v)))

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
        leggir = []
        while -p[find(0)] != n:
            if q.empty():
                break
            t = q.get()
            # print(t)
            (w, (u, v)) = t
            if find(u) == find(v):
                continue
            if u < v:
                leggir.append((u, v))
            else:
                leggir.append((v, u))
            W += w
            join(u, v)
            # print(p)

        if -p[find(0)] != n:
            print("Impossible")
        else:
            print(W)
            leggir.sort()
            for leg in leggir:
                (x, y) = leg
                print(x, y, sep=" ")

        (n, m) = tuple([int(x) for x in input().split()])


if __name__ == "__main__":
    main()
