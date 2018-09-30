from itertools import permutations

def gen_all_substrings(s):
    lt = lambda pair: pair[0] < pair[1]
    index_pairs = filter(lt, permutations(range(len(s)+1), 2))
    return (s[i:j] for i,j in index_pairs)

def get_all_substrings(s):
    return list(gen_all_substrings(s))

a=str(input().strip())
b=str(input().strip())
asub=get_all_substrings(a)
count=0
for i in asub:
	if(i in b):
		count+=1
print(count)
