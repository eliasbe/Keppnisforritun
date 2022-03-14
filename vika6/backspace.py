st = input()
q = []

for s in st:
    if s == "<":
        q.pop()
    else:
        q.append(s)

print("".join(q))
