@profile
def pok():
    T = int(input())
    for t in range(T):
        S, c = enom()
        print(S, c)


def enom():
    k = int(input())
    leikur = []
    munur = 0
    eftir = k
    S = -1
    a, b = (0, 0)
    for i in range(k):
        leikur.append([x == "E" for x in input().split()])
        if S < 0:
            # print()
            munur += leikur[-1][0]
            a += leikur[-1][0]
            # print(i, munur)
            if abs(munur) > eftir or -munur > eftir - 1:
                S = 2 * i + 1
                continue
            eftir -= 1
            munur -= leikur[-1][1]
            b += leikur[-1][1]
            # print(i, munur)
            if abs(munur) > eftir or i == k - 1:
                S = 2 * i + 2
                continue

    # print(S, a, b, sep="\t")

    y = S // 2
    x = y + S % 2
    even = x == y

    aleita = x - a != 0 and a != 0
    bleita = y - b != 0 and b != 0

    if not aleita and not bleita:
        return S, 0
    atemp = 0
    btemp = 0

    nulltarget = x - a
    astarget = a

    if not even:
        if a < b:
            nulltarget -= 1
        elif b < a:
            astarget -= 1
        if astarget == 0 or nulltarget == 0:
            aleita = False

    if aleita:

        for i in range(x):
            stak = leikur[i][0]

            if stak == 0:
                nulltarget -= 1
            elif stak == 1:
                astarget -= 1

            if nulltarget == 0 or astarget == 0:
                atemp = i * 2 + 1
                break

    nulltarget = y - b
    astarget = b
    if even:
        if b < a:
            nulltarget -= 1
        elif a < b:
            astarget -= 1
        if astarget == 0 or nulltarget == 0:
            bleita = False

    if bleita:

        for i in range(x):
            stak = leikur[i][1]

            if stak == 0:
                nulltarget -= 1
            elif stak == 1:
                astarget -= 1

            if nulltarget == 0 or astarget == 0:
                btemp = i * 2 + 2
                break

    return S, max(atemp, btemp)


if __name__ == "__main__":
    pok()

