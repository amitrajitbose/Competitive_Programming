def reduce_it(n,d):
	n = str(n) + str(d)
	s = list(n)
	new = []
	new.append(s[0]) #first digit
	l = len(s)

	for i in range(1,l):
		if(s[i] >= new[-1]):
			new.append(s[i])
		else:
			new.pop(-1)
			new.extend(s[i:])
			break
	if(len(new)==len(s)):
		new.pop(-1)
	num = ''.join(new)
	return (int(num))

def reducable(n):
	if(n<10):
		return False
	n=list(str(n))
	a=n[0]
	for i in n[1:]:
		if(a>i):
			return True
		a=i
	return False

t = int(input())
for testcase in range(t):
	n, d = map(int, input().strip().split())
	if(d < n%10):
		n = reduce_it(n,d)
	while(reducable(n)):
		n = reduce_it(n,d)
	print(n)