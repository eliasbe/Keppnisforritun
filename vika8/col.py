from collections import defaultdict
import queue


def main():
    (m, n) = tuple([int(x) for x in input().split()])
    d = defaultdict(list)
    hraefnalisti = list()
    for i in range(m):
        hraefnalisti.append([int(x) for x in input().split()[:-1]])
        for s in hraefnalisti[-1]:
            d[s].append(i)

    nagrannalisti = list()
    for i, l in enumerate(hraefnalisti):
        temp = set()
        for h in l:
            for nag in d[h]:
                if nag == i:
                    continue
                temp.add(nag)
        nagrannalisti.append(list(temp))

    def bipartite(naglist):
        q = queue.Queue()
        color = [-1 for i in range(m)]
        for i in range(len(naglist)):
            if color[i] != -1:
                continue
            q.put(i)
            color[i] = 0
            while not q.empty():
                current = q.get()
                for x in naglist[current]:
                    if color[x] == -1:
                        color[x] = 1 - color[current]
                        q.put(x)
                    elif color[x] == color[current]:
                        return False
        return True

    if bipartite(nagrannalisti):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
