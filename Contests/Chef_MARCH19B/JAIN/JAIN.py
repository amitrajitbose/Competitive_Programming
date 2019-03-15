from collections import defaultdict
tc = int(input())
for tcs in range(tc):
	n = int(input())
	freq_of = defaultdict(int)
	inputs = []
	extra = 0
	heros = 0
	for i in range(n):
		tmp = str(input().strip())
		tmp = sorted(list(set(list(tmp))))
		key = ''.join(tmp)
		if(len(key)==5):
			heros += 1
		else:
			freq_of[key] += 1
	
	inputs = list(freq_of.keys())
	#print(freq_of)
	m = len(inputs)
	cnt = 0

	for i in range(m-1):
		lcnt = 0
		for j in range(i+1,m):
			a = list(inputs[i])
			b = list(inputs[j])
			thislist = a+b
			if(len(set(thislist))==5):
				lcnt += freq_of[''.join(b)]
		cnt += (lcnt * freq_of[inputs[i]])
	# calculating contribution from heroes (jo akela kaafi h)
	for i in range(1,heros+1):
		extra += (n-i)
	print(cnt+extra)
	del freq_of

'''
2
4
aiou
oiu
aeo
oea
8
aeiou
uioe
e
aaiioue
aaeiou
aeiou
aeooiu
oiua
'''
'''
4
27
'''