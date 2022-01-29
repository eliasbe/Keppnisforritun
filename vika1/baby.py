bites = int(input())
line = input()
speech = line.split()
end = False
if len(speech) != bites:
    print("something is fishy")
else:
    for i in range(bites):
        if (speech[i] != str(i+1) and speech[i] != "mumble"):
            print("something is fishy")
            end = True 
            break
    if not end:
        print("makes sense")
