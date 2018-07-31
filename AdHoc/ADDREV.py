# Problem: https://www.spoj.com/IITRPRF1/problems/ADDREV/

def rev(n):
	st=str(n)
	st=st[::-1]
	s=int(st)
	return s

t=int(input())
for _ in range(t):
	m,n=[int(x) for x in input().strip().split()]
	s=rev(m) + rev(n)
	print(rev(s))