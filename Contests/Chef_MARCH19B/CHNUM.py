for _ in range(int(input())):
	n = int(input())
	arr = [int(x) for x in input().strip().split()]
	pc,nc,zc = 0, 0, 0
	for i in arr:
		if i<0:
			nc = nc+1
		else:
			pc = pc+1
	ans = [pc, nc]
	if 0 not in ans:
		print(max(ans),min(ans))
	else:
		print(n, n)
