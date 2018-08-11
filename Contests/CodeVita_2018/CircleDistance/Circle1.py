from math import ceil as halfroundup

def distance(x1,y1,x2,y2):
	return float(halfroundup((((x1-x2)**2)+((y1-y2)**2))**(1/2)))

def rotate(n,x):
	if(n==0):
		return (x,0)
	elif(n==1):
		return (0,x)
	elif(n==2):
		return (-1*x,0)
	elif(n==3):
		return (0,-1*x)

v1=int(input())
x1=int(input())
v2=int(input())
x2=int(input())
n=int(input())

v1=(v1*n)%360
v2=(v2*n)%360

(a,b)=rotate(v1/90,x1)
(c,d)=rotate(v2/90,x2)
dist=distance(a,b,c,d)

print("{0:.2f}".format(dist))