# Author : @amitrajitbose
for _ in range(int(input())):
  n,a,b = list(map(int,input().strip().split()))
  array = list(map(int,input().strip().split()))
  bob, alice, both = 0, 0, 0
  for i in array:
    if(i%a==0):
      bob += 1
    if(i%b==0):
      alice += 1
    if(i%a==0 and i%b==0):
      both += 1
  
  #SUBTASK 1
  if(a==b):
    if(bob>0):
      print("BOB")
    else:
      print("ALICE")
  #SUBTASK 2
  elif(both==0):
    if(bob > alice):
      print("BOB")
    elif(bob <= alice):
      print("ALICE")
  else:
    bob_has = bob - both
    alice_has = alice - both
    if(alice_has > bob_has):
        print("ALICE")
    elif(alice_has <= bob_has):
      print("BOB")