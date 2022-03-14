tala = int(input())

summa = 0
for i in range(8):
    summa += tala % 10 * (i % 6 + 2)
    tala = tala // 10

print(11 - summa % 11)
