'''
DCP #16
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
'''

class log(object):
	def __init__(self,N):
		self.log=[]
		self.size=0
		self.N=N
	def __str__(self):
		return str(self.log)[1:-1]
	def record(self, order_id):
		self.log.append(order_id)
		self.size+=1
		if(self.size == self.N+1):
			self.log.pop(0)
			self.size-=1
	def get_last(self,p):
		if(p==0):
			print("None")
			return
		print(*self.log[-p:])
	

log=log(10)
for x in range(20):
	log.record(x)
log.get_last(0)
log.get_last(1)
log.get_last(5)
log.record(20)
log.record(21)
log.get_last(1)
log.get_last(3)
log.get_last(0)
print(log)
'''
OUTPUT

None
19
15 16 17 18 19
21
19 20 21
None
12, 13, 14, 15, 16, 17, 18, 19, 20, 21

'''