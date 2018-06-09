#Problem: www.spoj.com/probleams/CANDY3/
test=int(input())
for _ in range(test):
	gapline=input()
	n=int(input())
	candies=0
	for i in range(n):
		c=int(input())
		candies+=c
		candies=candies%n
	if(candies==0):
		print("YES")
	else:
		print("NO")