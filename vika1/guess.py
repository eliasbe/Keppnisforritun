þak = 1001
golf = 0
gisk = 500
print(gisk)
inn = input()
while (inn!="correct"):
	if (inn == "lower"):
		þak = gisk	
		gisk = (gisk+golf)//2
		print(gisk)
		inn = input()
	if (inn == "higher"):
		golf = gisk
		gisk = (gisk+þak)//2
		print(gisk)
		inn = input()
#print(f"The number is {gisk}")
