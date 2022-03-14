# Restaurant Orders
#
# Input: 1 <= n <= 100, number of menu items
#        c1, ..., cn, cost of each item. ci <= 1000
#        m, number of orders
#        s1, ..., sm, cost of orders. si <= 30000
#
# Output: For each order:
#           If unique solution: list of numbers of the ordered items in ascending order
#           If multiple solutions: 'Ambiguous'
#           If no solution: 'Impossible'


def lookup(i, s, minnun, bakk, C):
    if s == 0:
        return 0
    elif s < 0:
        return 1
    elif i == len(minnun):
        return 1
    elif minnun[i][s] != -1:
        return minnun[i][s]
    vera = lookup(i, s - C[i], minnun, bakk, C)
    fara = lookup(i + 1, s, minnun, bakk, C)
    global jafnt
    if vera == 0 and fara == 0:
        jafnt = True
    if vera < fara:
        bakk[i][s] = 0
    else:
        bakk[i][s] = 1
    minnun[i][s] = min(vera, fara)
    return min(vera, fara)


def orders(C, S):
    for o in range(len(S)):
        minnun = [[-1 for i in range(30001)] for j in range(len(C))]
        bakk = [[-1 for i in range(30001)] for j in range(len(C))]
        global jafnt
        jafnt = False

        lookup(0, S[o], minnun, bakk, C)

        if minnun[0][S[o]] != 0:
            print("Impossible")
        elif jafnt:
            print("Ambiguous")
        else:
            order = []

            ess = S[o]
            i = 0
            while ess > 0:
                if bakk[i][ess] == 0:
                    order.append(i + 1)
                    ess -= C[i]
                else:
                    i += 1
            order.sort()
            print(*order)


def main():
    n = int(input())
    C = [int(c) for c in input().split()]
    m = int(input())
    S = [int(s) for s in input().split()]

    assert n == len(C) and m == len(S)
    global jafnt

    orders(C, S)


if __name__ == "__main__":
    main()
