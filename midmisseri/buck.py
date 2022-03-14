hnit = tuple(int(x) for x in input().split())
n = int(input())

(x1, x2, y1, y2) = hnit

count = 0

for i in range(n):
    (x, y) = tuple(int(a) for a in input().split())
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        count += 1

print(count)
