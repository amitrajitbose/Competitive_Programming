'''
The classical job sequencing problem with deadline, solved using greedy approach.
'''

n=int(input("ENTER NUMBER OF JOBS : "))
arr=[]
maxdeadline=0
for i in range(n):
	p,d=[int(x) for x in input("ENTER PROFIT AND DEADLINE OF JOB : ").strip().split()]
	arr.append((i+1,p,d))
	maxdeadline=max(maxdeadline,d)

# Sort with decreasing order of profits
arr=sorted(arr, key=lambda x: x[1], reverse=True)
# Maximum time-slots possible for jobs to be done
slots=[-1 for x in range(maxdeadline+1)]
# Iterating over sorted list
finalprofit=0
for i in arr:
	if(slots[i[2]]==-1):
		# Slot empty, we will do this job because it is most profitable
		slots[i[2]]=i[0] # Assigning with the job number
		finalprofit+=i[1]
	else:
		# Slot taken by some other job
		# Check if the job can be finished earlier
		# If there is some vacant spot
		for j in range(i[2]-1,0,-1):
			if(slots[j]==-1):
				slots[j]=i[0] # Assign that job
				finalprofit+=i[1]
				break

print("\nOPTIMAL SEQUENCE IS: ")
for i in range(1,maxdeadline+1):
	print("Perform Job %d In Time Slot %d" % (slots[i],i))
print("\nMAXIMUM TOTAL PROFIT = ",finalprofit)

'''
OUTPUTS:

ENTER NUMBER OF JOBS : 7
ENTER PROFIT AND DEADLINE OF JOB : 35 3
ENTER PROFIT AND DEADLINE OF JOB : 30 4
ENTER PROFIT AND DEADLINE OF JOB : 25 4
ENTER PROFIT AND DEADLINE OF JOB : 20 2
ENTER PROFIT AND DEADLINE OF JOB : 15 3
ENTER PROFIT AND DEADLINE OF JOB : 12 1
ENTER PROFIT AND DEADLINE OF JOB : 5 2

OPTIMAL SEQUENCE IS: 
Perform Job 4 In Time Slot 1
Perform Job 3 In Time Slot 2
Perform Job 1 In Time Slot 3
Perform Job 2 In Time Slot 4

MAXIMUM TOTAL PROFIT =  110





ENTER NUMBER OF JOBS : 5
ENTER PROFIT AND DEADLINE OF JOB : 20 2
ENTER PROFIT AND DEADLINE OF JOB : 15 2
ENTER PROFIT AND DEADLINE OF JOB : 10 1
ENTER PROFIT AND DEADLINE OF JOB : 5 3
ENTER PROFIT AND DEADLINE OF JOB : 1 3

OPTIMAL SEQUENCE IS: 
Perform Job 2 In Time Slot 1
Perform Job 1 In Time Slot 2
Perform Job 4 In Time Slot 3

MAXIMUM TOTAL PROFIT =  40
'''