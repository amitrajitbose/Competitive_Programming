var={
	0:'A',
	1:'B',
	2:'C',
	3:'D',
	4:'E',
	5:'F',
	6:'G'
}

path=[('A',1,0),
		('B',3,2),
		('C',4,3),
		('D',2,5),
		('E',6,6),
		('F',0,4),
		('G',6,1)]

blackjump=[[0,1,3,2,4,6,5],
			[1,3,2,4,6,5,0],
			[2,4,6,5,0,1,3],
			[3,2,4,6,5,0,1],
			[4,6,5,0,1,3,2],
			[5,0,1,3,2,4,6],
			[6,5,0,1,3,2,4]
			]

t=int(input())
for _ in range(t):
	s=str(input())
	steps=list(s)
	curr=0 #start at A
	for i in range(len(steps)):
		x=int(steps[i])
		#follow black
		x=x%7
		curr=blackjump[curr][x]
		#print(var[curr])
		#go one white
		curr=path[curr][2]
		#print(var[curr])
		#print("--")
	print(var[curr])
