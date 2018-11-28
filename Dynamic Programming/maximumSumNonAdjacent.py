'''
Given an array of integers, find a maximum sum of non-adjacent elements.

For example, inputs [1, 0, 3, 9, 2] should return 10 (1 + 9).

The question has been asked by Uber recently.
'''
# My Article : https://medium.com/@amitrajitbose/hello-readers-geeks-techies-coders-bbbcb246882

def maxSum2(arr):
	#BOTTOM UP APPROACH
	cache=[0 for x in range(len(arr))]
	cache[0]=arr[0]
	cache[1]=max(arr[0],arr[1])
	for i in range(2,len(arr)):
		cache[i]=max(cache[i-1], arr[i]+cache[i-2])
	return (cache[-1])

print(maxSum2([1,0,3,9,2])) #10
print(maxSum2([5,1,1,5])) #10
print(maxSum2([2,4,6,2,5])) #13