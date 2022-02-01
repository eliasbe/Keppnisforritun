def veci():
    l = [int(x) for x in list(input())]
    temp = []
    for i in range(len(l) - 1, 0, -1):
        if l[i] > l[i - 1]:
            fulcrum = l[i - 1]
            temp.append(l[i - 1])
            temp.append(l[i])
            temp.sort()
            for j in temp:
                if j > fulcrum:
                    l[i - 1] = j
                    temp.remove(j)
                    break
            return l[:i] + temp
        else:
            temp.append(l[i])
    return [0]


print("".join([str(x) for x in veci()]))
