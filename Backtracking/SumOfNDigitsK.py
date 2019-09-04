"""
You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.

Input Format
The single line of the input contains a pair of integers m, s — the length and the sum of the digits of the required numbers.

Constraints
1 ≤ m ≤ 100 0 ≤ s ≤ 900

Output Format
In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).

Sample Input
2 15
Sample Output
69 96
"""


global result

def findNDigitNumsUtilMAX(n, sum, out,index):
	if len(result) == 1 and result[0][0]!='0':
		return
	elif len(result) == 1 and result[0][0]=='0':
		result.pop(0)

	# Base case 
	if (index > n or sum < 0): 
		return

	f = "" 
	
	# If number becomes N-digit 
	if (index == n): 
	
		# if sum of its digits is equal 
		# to given sum, print it 
		if(sum == 0): 
			out[index] = "" 
			
			for i in out: 
				f = f + i
			result.append(f)
			#return f #print(f, end = " ")
		return

	# Traverse through every digit. Note 
	# that here we're considering leading 
	# 0's as digits 
	for i in range(9,-1,-1): 
		
		# append current digit to number 
		out[index] = chr(i + ord('0')) 

		# recurse for next digit with reduced sum 
		findNDigitNumsUtilMAX(n, sum - i, out, index + 1) 

def findNDigitNumsUtil(n, sum, out,index):
	if len(result) == 1 and result[0][0]!='0':
		return
	elif len(result) == 1 and result[0][0]=='0':
		result.pop(0)

	# Base case 
	if (index > n or sum < 0): 
		return

	f = "" 
	
	# If number becomes N-digit 
	if (index == n): 
	
		# if sum of its digits is equal 
		# to given sum, print it 
		if(sum == 0): 
			out[index] = "" 
			
			for i in out: 
				f = f + i
			result.append(f)
			#return f #print(f, end = " ")
		return

	# Traverse through every digit. Note 
	# that here we're considering leading 
	# 0's as digits 
	for i in range(10): 
		
		# append current digit to number 
		out[index] = chr(i + ord('0')) 

		# recurse for next digit with reduced sum 
		findNDigitNumsUtil(n, sum - i, out, index + 1)

# This is mainly a wrapper over findNDigitNumsUtil. 
# It explicitly handles leading digit 
def findNDigitNums( n, sum): 

	# output array to store N-digit numbers 
	out = [False] * (n + 1) 

	# fill 1st position by every digit 
	# from 1 to 9 and calls findNDigitNumsUtil() 
	# for remaining positions 
	for i in range(10): 
		out[0] = chr(i + ord('0')) 
		findNDigitNumsUtil(n, sum - i, out, 1)

def findNDigitNumsMAX( n, sum): 

	# output array to store N-digit numbers 
	out = [False] * (n + 1) 

	# fill 1st position by every digit 
	# from 1 to 9 and calls findNDigitNumsUtil() 
	# for remaining positions 
	for i in range(9,-1,-1): 
		out[0] = chr(i + ord('0')) 
		findNDigitNumsUtilMAX(n, sum - i, out, 1)

result = []
n,sum = [int(x) for x in input().strip().split()]
findNDigitNums(n, sum)
if len(result) > 0:
	minm = result[0]
	result.pop(0)
else:
	minm = -1

findNDigitNumsMAX(n, sum)
if len(result) > 0:
	maxm = result[0]
else:
	maxm = -1
print(minm, maxm)

