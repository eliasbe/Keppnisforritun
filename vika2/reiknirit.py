
def main():
    print(cnt())

def cnt():
    n = int(input())
    line = input()
    tölur = [int(x) for x in line.split()]

    assert(len(tölur) == n)

    if len(set(tölur)) == 1:
        return n

    tölur.sort()
    fjöldi = list()

    s = n
    m = n
    end = n-1
    gildi = tölur[end]
    while end >= 0:
        g = gildi
        count = 1
        while g == gildi:
            g = tölur[end-count]
            count += 1
        count -= 1
        end = end-count
        #m = m-count
        #s += m
        gildi = g
        fjöldi.append(count)

    fjöldi.sort()
    for f in reversed(fjöldi):
       m -= f
       s += m

    return s
    
    
if __name__=="__main__":
    main()





