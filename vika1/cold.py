nr = input()
line = input()
split = line.split()
assert(len(split) == int(nr))
count = 0
for i in range(len(split)):
    if int(split[i]) < 0:
        count += 1
print(count)
