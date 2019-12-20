from collections import Counter
for _ in range(int(input())):
	p = str(input())
	h = str(input())
	if (len(p) > len(h)):
		print("NO")
		continue
	if (len(p) == len(h)):
		if sorted(p)==sorted(h):
			print("YES")
		else:
			print("NO")
		continue
	
	window = Counter(p)
	s = len(p)
	flag = 0
	curr = Counter(h[:s]) # first window
	i = 0
	while i+s <= len(h):
		#print("Current Window: ", h[i:i+s], curr)

		if i>0:
			curr[h[i-1]] -= 1 # remove the prev char
			curr[h[i+s-1]] += 1 # add new next char
			if curr[h[i-1]] == 0:
				del curr[h[i-1]] # remove the key
		
		
		
		if curr == window:
			print("YES")
			flag = 1
			break
		i += 1
	if flag == 0:
		print("NO")

