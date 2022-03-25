def main():
    mod = 10 ** 9 + 7
    n = int(input())
    li = [int(x) for x in input().split()]
    assert len(li) == n

    asar = 0
    tvist = 0
    summa = 0
    for l in li:
        if l == 1:
           asar += 1
        elif l == 2:
            # Get valið alla sömu kosti og áður með eða án þessum tvisti
            # Eða þetta getur verið fyrsti tvisturinn á jafn marga vegu og
            # það eru margir ásar á undan honum
            tvist = 2*tvist + asar
            tvist %= mod
        elif l == 3:
            # Get endað hér með þá möguleika sem komnir eru
            summa += tvist
            summa %= mod

    print(summa)
        

if __name__ == '__main__':
    main()
