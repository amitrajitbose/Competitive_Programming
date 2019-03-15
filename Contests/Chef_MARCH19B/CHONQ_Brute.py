from math import floor
for _ in range(int(input())):
	n,k=map(int,input().strip().split())

	ar=[int(x) for x in input().strip().split()]
	a=[0]
	for i in ar:
		a.append(i)

	# Core calculation: Greedy
	spot=n+1
	for i in range(1,n+2):
		#print("\n\nEnter At Pos",i)
		cost = 0
		for j in range(i,n+1):
			#print("(",a[j],"/",(j-i+1),end=") + ")
			cost += floor(a[j]/(j-i+1))
		#print("\n")
		#print("COST",cost)
		if(cost<=k):
			spot=min(spot,i)
			break
	print(spot)
