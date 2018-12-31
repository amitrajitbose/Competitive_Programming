'''
DCP #19

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of 
K different colors. He has a goal of minimizing cost while 
ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents 
the cost to build the nth house with kth color, return the minimum 
cost which achieves this goal.

'''
def color(n,k, costmatrix=[[]]):
	cost = [[0 for i in range(k)] for j in range(n)]
	'''
	row = house number
	column = color used
	cost of painting the first row will be trivial
	'''
	#for i in range(k):
	cost[0] = costmatrix[0][:]
	'''
	cost of painting further building will be depending upon
	previous colors chosen
	'''
	for house in range(n):
		for col in range(k):
			previous = cost[house-1][:col] + cost[house-1][col+1:] #cannot be of same color
			cost[house][col] = costmatrix[house][col] + min(previous)
	return min(cost[-1]) #last row in the cost of coloring n houses

cost_func = [[4,0,3],[8,3,8],[4,5,0],[3,4,4],[8,8,0]]
print(color(5,3,cost_func)) # 9