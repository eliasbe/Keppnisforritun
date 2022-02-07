# A Question of Ingestion
#
# Input: n, m (n<=100, m<= 20000)
# n: number of courses
# m: Calories Stan can eat in the first hour
# c_1 ... c_n, calories of each course
#
# Stan's appetite decreases by a factor of 2/3 every hour
# If he skips one meal his appetite doesn't decrease
# If he skips two meals it's back to m
#
# Output: maximum number of calories Stan can consume

n, m = tuple(int(x) for x in input().split())
c = [int(x) for x in input().split()]
assert len(c) == n


# Forreikna r gildi
s = m
R = []
while s > 0:
    R.append(s)
    s = (2 * s) // 3
R.append(0)

matrix = [[-1 for j in range(len(R) + 1)] for i in range(n)]


def k(i, r):
    if r > len(R) - 1:
        r = len(R) - 1
    if i == n - 1:
        return min(R[r], c[i])
    if i > n - 1:
        return 0
    if matrix[i][r] != -1:
        return matrix[i][r]
    kostur1 = min(R[r], c[i]) + k(i + 1, r + 1)
    kostur2 = k(i + 1, max(0, r - 1))
    kostur3 = k(i + 2, 0)
    matrix[i][r] = max(kostur1, kostur2, kostur3)
    return matrix[i][r]


print(k(0, 0))
