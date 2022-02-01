def tables():
    n = int(input())
    line = input()
    tölur = [int(x) for x in line.split()]
    assert len(tölur) == n

    tölur.sort()
    s = 0
    for i in range(n - 1):
        s += pow(abs(tölur[i] - tölur[i + 1]), 2)

    return s


print(tables())
