'''
Challenged by : @iamriddhi
Given a string expression which consists only ‘}’ and ‘{‘. 
The expression may not be balanced. You need to find the minimum 
number of bracket reversals which are required to make the expression balanced.
Return -1 if the given expression can't be balanced.

Input Format :
String S
Output Format :
Required count
Sample Input 1 :
{{{
Sample Output 1 :
-1
Sample Input 2 :
{{{{}}
Sample Output 2 :
1
'''
from math import ceil
def minimum_reversals(s):
	'''
	Input : String
	Output : Integer
	'''
	stack=[]
	for ch in s:
		if(ch=='{'):
			stack.append(ch) # PUSH
		else:
			if(len(stack)==0 or stack[-1]=='}'):
				stack.append(ch) # PUSH
			elif(stack[-1]=='{'):
				stack.pop() #POP
	# now the stack contains only unbalanced parenthesis
	split = 0
	print(stack) #DEBUG
	n = len(stack)
	if(n==0):
		return 0 #ALREADY BALANCED
	else:
		while(len(stack) and stack[-1]!='}'):
			stack.pop()
			split+=1
		if(n%2):
			return -1
		else:
			return ceil((n-split)/2) + ceil(split/2)


for _ in range(int(input())):
	s=str(input())
	print(minimum_reversals(s))
