from collections import defaultdict


def count_extra_contrib(sufficient_count, n):
	extra = 0
	for i in range(sufficient_count):
		extra += (n-(i+1))
	return extra

for _ in range(int(input())):
	n = int(input())
	count_of_pattern = defaultdict(int)
	non_sufficient_patterns = []
	extra = 0
	cnt = 0
	sufficient_count = 0
	for i in range(n):
		tmp = str(input().strip())
		tmp = sorted(list(set(list(tmp))))
		key = ''.join(tmp)
		if(len(key)==5):
			sufficient_count += 1
		else:
			count_of_pattern[key] += 1
	
	non_sufficient_patterns = list(count_of_pattern.keys())
	m = len(non_sufficient_patterns)

	for i in range(m-1):
		lcnt = 0
		for j in range(i+1,m):
			a = list(non_sufficient_patterns[i])
			b = list(non_sufficient_patterns[j])
			final_dish = a+b
			if(len(set(final_dish))==5):
				lcnt += count_of_pattern[non_sufficient_patterns[j]]
		cnt += (lcnt * count_of_pattern[non_sufficient_patterns[i]])
	
	
	
	del count_of_pattern
	print(cnt+count_extra_contrib(sufficient_count, n))
