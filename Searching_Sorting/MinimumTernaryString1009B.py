#Problem: https://codeforces.com/contest/1009/problem/B
#THIS FAILS TO CLEAR TC #4

stack=[] #primary stack
tempstack=[] #secondary stack
s=list(input())

l=len(s)
stack.append(s[0])

for i in range(1,l):
	a=ord(s[i])
	b=ord(stack[-1])

	if((a-b)==1 or abs(a-b)==2 or (a==b)):
		stack.append(s[i])
		#print(stack)
	elif((b-a)==1):
		while((b-a)==1):
			tempstack.append(stack.pop())
			if(len(stack)>0):
				b=ord(stack[-1])
			else:
				break
		stack.append(s[i])
		while(len(tempstack)>0):
			stack.append(tempstack.pop())
		#print(stack)

print(''.join(stack))
