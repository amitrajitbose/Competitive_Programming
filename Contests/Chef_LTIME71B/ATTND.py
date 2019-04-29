for _ in range(int(input())):
	names = []
	namedict = {}
	for i in range(int(input())):
		fn,sn = [str(x) for x in input().strip().split()]
		names.append((fn,sn))
		if fn in namedict:
			namedict[fn] += 1
		else:
			namedict[fn] = 1
	for i in names:
		if namedict[i[0]]==1:
			print(i[0])
		else:
			print(i[0],i[1])

