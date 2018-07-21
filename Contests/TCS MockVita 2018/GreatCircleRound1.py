#MockVita 2 Problem: Great Circle

pi=3.1415625
circum=2*pi*6400

def circumDifference(A,B):
	a,b,c,d=A[0],A[1],B[0],B[1]
	if(a==90 and c==90) or (a==-90 and c==-90):
	    diff=0
	#check if one is north pole or south pole and another on equator line
	elif(A==(90,0) and B[0]==0) or (A==(-90,0) and B[0]==0):
		diff=0.25
	elif(B==(90,0) and A[0]==0) or (B==(-90,0) and A[0]==0):
		diff=0.25
	else:
		diff=(abs(a-c)+abs(b-d))/360
	
	return (diff*circum)

n=int(input())
inputs=[]

for i in range(n):
	lati,longi=[str(x) for x in input().strip().split(',')]
	latiVal=int(lati[0:len(lati)-1]) #contains the value of latitude
	latiDir=lati[-1] #contains N or S
	longiVal=int(longi[0:len(longi)-1]) #value of longitude
	longiDir=longi[-1] #contain E or W
	#I have considered N and E as my parameter standard. So I convert them accordingly.
	if(latiDir=='S'):
		latiVal= -1 * latiVal
	if(longiDir=='W'):
		longiVal= -1 * longiVal
	inputs.append((latiVal,longiVal))

totalSum=0 #keeps track of the total required answer

for i in range(n-1):
	src=inputs[i]
	dest=inputs[i+1]
	totalSum+=circumDifference(src,dest)
	#print(">>",totalSum/pi)
print(round(totalSum))
