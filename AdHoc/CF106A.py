trump = str(input())
carda, cardb = [str(x) for x in input().strip().split()]
win = 0
deck = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ranka = deck.index(carda[0])
rankb = deck.index(cardb[0])
if(carda[1]==cardb[1]):
	#same suit
	if(ranka > rankb):
		win=1
	elif(ranka < rankb):
		win=2
else:
	if(carda[1]==trump[0]):
		win=1
	elif(cardb[1]==trump[0]):
		win=2

if(win==1):
	print("YES")
else:
	print("NO")

