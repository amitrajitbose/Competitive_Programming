'''
Dual Stack Sort
Ascending Order
Lexicographic Order
Sort a string of alphanumeric or only alphabet or only numeric in their lexicographic order.
----------------------
Author: Amitrajit Bose
'''


stack=[] #primary stack
tempstack=[] #secondary stack
s=list(input("Enter The String of Characters/Digits [Without Spaces]: "))

l=len(s)
stack.append(s[0])

for i in range(1,l):
	a=ord(s[i])
	b=ord(stack[-1]) #Top Of Stack

	if((a-b)>=1 or (a==b)):
		stack.append(s[i])
		#print(stack)
	elif((b-a)>=1):
		while((b-a)>=1):
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