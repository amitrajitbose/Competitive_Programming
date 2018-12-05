'''
DCP #14

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

Approach: Monte Carlo Algorithm
'''
import random
def approximate_pi(iterations=10000):
	total=0
	inside=0
	for i in range(iterations):
		x=random.uniform(0,1)-0.5
		y=random.uniform(0,1)-0.5
		if((x**2)+(y**2))<=0.25:
			#then inside the circle
			inside+=1
		total+=1
	ratio=inside/total
	#area of circle = ratio*area of square=>pi*0.5*0.5=1*1*ratio
	return ratio*4

print("APPROXIMATED VALUE OF PI: {0:.3f}".format(approximate_pi()))
