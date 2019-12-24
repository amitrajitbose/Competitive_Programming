# Count and say sequence

def countnsay(seq):
	res = ''
	n = len(seq)
	i = 0
	while i < n:
		cnt = 1
		while i<n-1 and seq[i] == seq[i+1]:
			cnt += 1
			i += 1
		res += str(cnt) + seq[i]
		i += 1
	return res

def solve(n):
	i = '1'
	for j in range(2, n+1):
		i = countnsay(i)
	return i

print(solve(7))
