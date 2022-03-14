import queue


def main():
    (upp, down) = tuple([int(x) for x in input().split()])
    (r, c) = tuple([int(x) for x in input().split()])
    roof = []
    for i in range(r):
        roof.append([int(x) for x in input().split()])
    (x_target, y_target) = tuple([int(x) for x in input().split()])

    def co_map(x, y):
        return c * x + y

    def idx_map(i):
        x = i // c
        y = i % c
        return (x, y)

    def get_neighbors(i):
        granni = []
        (x, y) = idx_map(i)
        height = roof[x][y]
        if x > 0:
            north_height = roof[x - 1][y]
            if north_height > height:
                if (north_height - height) <= upp:
                    granni.append(co_map(x - 1, y))
            else:
                if (height - north_height) <= down:
                    granni.append(co_map(x - 1, y))
        if x < r - 1:
            south_height = roof[x + 1][y]
            if south_height > height:
                if (south_height - height) <= upp:
                    granni.append(co_map(x + 1, y))
            else:
                if (height - south_height) <= down:
                    granni.append(co_map(x + 1, y))

        if y > 0:
            west_height = roof[x][y - 1]
            if west_height > height:
                if (west_height - height) <= upp:
                    granni.append(co_map(x, y - 1))
            else:
                if (height - west_height) <= down:
                    granni.append(co_map(x, y - 1))

        if y < c - 1:
            east_height = roof[x][y + 1]
            if east_height > height:
                if (east_height - height) <= upp:
                    granni.append(co_map(x, y + 1))
            else:
                if (height - east_height) <= down:
                    granni.append(co_map(x, y + 1))

        return granni

    def bfs(start, end):
        q = queue.Queue()
        q.put(start)
        d = [False for i in range(r * c)]
        while not q.empty():
            current = q.get()
            d[current] = True
            neighbors = get_neighbors(current)
            for neigh in neighbors:
                if neigh == end:
                    return True
                if d[neigh]:
                    continue
                q.put(neigh)
        return False

    lupp = bfs(0, co_map(x_target - 1, y_target - 1))
    liður = bfs(co_map(x_target - 1, y_target - 1), 0)

    if lupp and liður:
        print("Kvoldinu er bjargad!")
    else:
        print("Nu er Eyleifur i bobba!")


if __name__ == "__main__":
    main()
