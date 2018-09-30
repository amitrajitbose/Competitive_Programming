t=int(input())
for _ in range(t):
	n=int(input())
	if(n<60):
		print("NO")
	else:
		if(360/(180-n)==360//(180-n)):
			print("YES")
		else:
			print("NO")