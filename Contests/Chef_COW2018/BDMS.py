def bdms(n,k):
	if(n==0):
		return 0
	else:
		# n not zero
		if(n%2==0):
			kick = n//2
			n2 = kick
			n1 = 0
		else:
			kick = (n//2) + 1
			n2 = kick-1
			n1 = 1
		if(kick%k==0):
			return kick
		else:
			while(kick%k != 0 and n2>0):
				kick+=1
				n2-=1
				n1+=2
				if(n2==0):
					return -1
			return kick


n,k=[int(x) for x in input().strip().split()]
ans=bdms(n,k)
print(bdms(n,k))