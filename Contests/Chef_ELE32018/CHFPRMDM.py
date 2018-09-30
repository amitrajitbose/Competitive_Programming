# https://www.codechef.com/ELE32018/problems/CHFPRMDM
# author: Amitrajit Bose

#from pprint import pprint as pp

# function to generate an array of prime number using sieve
# returns boolean array of size n+1
def sieve(n):
	prime = [True for i in range(n+1)]
	p=2
	while(p * p <= n):
		# If prime[p] is not changed, then it is a prime
		if (prime[p] == True):
			# Update all multiples of p
			for i in range(p * 2, n+1, p):
				prime[i] = False
		p+=1
	prime[1]=False # 1 is not prime
	# assuming prime[0]=True
	return prime

# adds two tuples
def tupleAdd(t1,t2):
	return (t1[0]+t2[0],t1[1]+t2[1])

def findmax(arr,cache,n,prime):
	maxlen=0
	#marking the first top corner [0,0]
	if(prime[arr[0]]):
		cache[0][0]=(1,0)
		maxlen=1
	else:
		cache[0][0]=(0,1)
	
	#marking the first row, all subarrays starting from first character i=0
	#and also marking the diagonal elements
	for j in range(1,n):
		if(prime[arr[j]]):
			cache[0][j]=tupleAdd(cache[0][j-1],(1,0))
			cache[j][j]=(1,0)
			maxlen=1
		else:
			cache[0][j]=tupleAdd(cache[0][j-1],(0,1))
			cache[j][j]=(0,1)
		
		if(cache[0][j][0] > cache[0][j][1]):
			maxlen=max(maxlen,j+1)
	
	for i in range(1,n):
		for j in range(i+1,n):
			if(prime[arr[j]]):
				cache[i][j]=tupleAdd(cache[i][j-1],(1,0))
			else:
				cache[i][j]=tupleAdd(cache[i][j-1],(0,1))
			if(cache[i][j][0] > cache[i][j][1]):
				maxlen=max(maxlen,(j+1-i))
	#pp(cache)
	return maxlen

def main():
	prime = sieve(1000000)
	t=int(input())
	for _ in range(t):
		n=int(input())
		arr=[int(x) for x in input().strip().split()]
		cacherow = ([0]*n) # temporary
		cache = [[0 for x in range(n)] for x in range(n)]
		#cache initialised OK
		print(findmax(arr,cache,n,prime))


if __name__=='__main__':
	main()