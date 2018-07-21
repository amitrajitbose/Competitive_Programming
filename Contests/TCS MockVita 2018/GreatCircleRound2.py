from math import radians, cos, sin, asin, sqrt
pi=3.1415625
circum=6400
#haversine formula
def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a)) 
      
    # calculate the result
    return(c * circum)

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
    totalSum+=distance(src[0],dest[0],src[1],dest[1])
    #print(">>",totalSum/pi)
print(round(totalSum))