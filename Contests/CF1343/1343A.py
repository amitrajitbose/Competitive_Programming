from bisect import bisect_left as bs
def prefetch():
	lis = []
	s = 0
	p = 0
	x = 0
	while s < 10**9:
		s += (2**p)
		p += 1
		lis.append(s)
	return lis

def main():
	lhs = prefetch()
	for _ in range(int(input())):
		n = int(input().strip())
		ind = bs(lhs, n)
		for i in range(ind, -1, -1):
			if(n % lhs[i] == 0):
				print(n//lhs[i])
				break
main()

