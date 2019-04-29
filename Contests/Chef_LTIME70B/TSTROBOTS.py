for _ in range(int(input())):
	n,m = [int(x) for x in input().strip().split()]
	stk = []
	visited = {m:True}
	uniq = 1
	steps = list(input())
	curr = m
	for i in steps:
		if i=='L':
			curr-=1
		elif i=='R':
			curr+=1

		if curr not in visited:
			uniq+=1
			visited[curr]=True
	print(uniq)

