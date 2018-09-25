class Count:
	i=0
def knapsack(cap, n, items, table):
	Count.i += 1
	if(not table[cap][n] == -1):
		return table[cap][n]
	elif(n==0 or cap==0):
		table[cap][n]=0
	elif(items[n][1] > cap):
		table[cap][n]=knapsack(cap,n-1,items,table)
	else:
		reject=knapsack(cap,n-1,items,table)
		consider=knapsack(cap-items[n][1],n-1,items,table)+items[n][0]
		table[cap][n]=max(consider,reject)	
	return table[cap][n]

def main():
	n=int(input("ENTER  TOTAL NUMBER OF ITEMS: "))
	bagmax=int(input("ENTER CAPACITY OF BAG: "))
	items = [(0,0)]
	for i in range(n):
		print("ENTER VALUE & WEIGHT: ")
		a,b=[int(x) for x in input().strip().split()]
		items.append((a,b))

	cache = [[-1 for x in range(n+1)] for x in range(bagmax+1)]
	print("MAXIMUM WEIGHT: " , knapsack(bagmax, n, items, cache))
	print("TOTAL FUNCTION CALLS: ",Count.i)

if __name__=="__main__":
	main()