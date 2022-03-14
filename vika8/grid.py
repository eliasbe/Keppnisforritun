def main():
    import queue

    q = queue.Queue()

    (n, m) = tuple([int(x) for x in input().split()])
    grid = []
    for i in range(n):
        grid.append([int(x) for x in input()])
    d = [-1 for i in range(n * m)]

    def co_map(x, y):
        return m * x + y

    def idx_map(i):
        x = i // m
        y = i % m
        return (x, y)

    q.put(0)
    d[0] = 0

    def get_neighbors(i):
        (x, y) = idx_map(i)
        skref = grid[x][y]
        neighbors = []
        if x >= skref:
            neighbors.append(co_map(x - skref, y))
        if y >= skref:
            neighbors.append(co_map(x, y - skref))
        if (skref + x) < n:
            neighbors.append(co_map(x + skref, y))
        if (y + skref) < m:
            neighbors.append(co_map(x, y + skref))

        return neighbors

    while not q.empty():
        current = q.get()
        neighbors = get_neighbors(current)
        for neigh in neighbors:
            if d[neigh] != -1:
                continue
            d[neigh] = d[current] + 1
            q.put(neigh)

    print(d[-1])


if __name__ == "__main__":
    main()
