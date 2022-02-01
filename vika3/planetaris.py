def battle():
    n, a = input().split()
    n = int(n)
    a = int(a)

    finn = [int(x) for x in input().split()]

    assert len(finn) == n

    finn.sort()
    count = 0
    for f in finn:
        if a < f + 1:
            break
        a -= f + 1
        count += 1

    return count


print(battle())
