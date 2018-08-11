from math import floor

def powerGenerated(radius, windspeed, efficiency):
	return (0.5*1.23*2*radius*radius*(windspeed**3)*efficiency)

def totalPower(unitsA,powerA,unitsB,powerB):
	return ((unitsA*powerA)+(unitsB*powerB))

#__main__
radiusA = float(input())
costA = float(input())
efficiencyA = float(input())
radiusB = float(input())
costB = float(input())
efficiencyB = float(input())
budget = float(input())
land = float(input())
windspeed = float(input())

powerA=powerGenerated(radiusA,windspeed,efficiencyA)
powerB=powerGenerated(radiusB,windspeed,efficiencyB)
powerpercostA=powerA/costA
powerpercostB=powerB/costB
#print(powerpercostA,powerpercostB) #debug

if(powerpercostA>powerpercostB):
	areaA=(2*radiusA*radiusA)
	areaB=(2*radiusB*radiusB)
	unitsA=floor(land/areaA)
	unitsB=floor((land-(unitsA*areaA))/areaB)

	
	initialtotalpower=totalPower(unitsA-1,powerA,unitsB,powerB)
	newB=floor((land-((unitsA-1)*areaA))/areaB)
	newtotalpower=totalPower(unitsA-1,powerA,newB,powerB)
	#print(">>> ",initialtotalpower,unitsA,unitsB)
	while(newtotalpower>=initialtotalpower and unitsA>=0 and unitsB>=0):
		initialtotalpower=newtotalpower
		unitsA-=1
		unitsB=floor((land-(unitsA*areaA))/areaB)
		#print(">>> ",newtotalpower,unitsA,unitsB)
		newB=floor((land-((unitsA-1)*areaA))/areaB)
		newtotalpower=totalPower(unitsA-1,powerA,newB,powerB)
	print("TOTAL ",initialtotalpower,unitsA,unitsB)

