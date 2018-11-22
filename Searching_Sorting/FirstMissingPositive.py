'''
DCP #4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Approach:
Part 1: Negative numbers do not contribute to the answer, so we separate them to one side of the array and 
remove the negative elements from left
Part 2: Run the following algorithm on the positive part of the array
1) Traverse the array arr[]
i) If arr(i) >= arr.length : IGNORE
ii)If arr(abs(arr(i))-1) = Negative : IGNORE
iii)Else, arr(abs(arr(i))-1) *= -1 MAKE IT NEGATIVE
2) Traverse the array arr[] again
i) If arr(i) > 0 : RETURN i+1 index, END
3) RETURN arr.length +1
'''

# Note that we cannot use a function, because passing the array will create a copy which we want to avoid
# Because requirement says constant space O(1)

def main():
	arr=[int(x) for x in input().strip().split()]
	n=len(arr)
	#segregation process
	j=0
	for i in range(n):
		if(arr[i]<=0):
			arr[i],arr[j]=arr[j],arr[i] #swap
			j+=1

	#removing negative values from left end
	for i in range(j):
		arr.pop(0)
	
	n=len(arr)
	#apply our finding algorithm
	for i in range(n):
		if(abs(arr[i])-1<n and arr[abs(arr[i])-1]>0):
			arr[abs(arr[i]) -1] = - 1 * arr[abs(arr[i]) -1]
	
	found=False
	for i in range(n):
		if(arr[i]>0):
			found=True
			print(i+1)
			break
	if(not found):
		print(n+1)

if __name__ == '__main__':
	main()

# ALL TEST CASES PASSED
# ALL CONSTRAINTS FOLLOWED