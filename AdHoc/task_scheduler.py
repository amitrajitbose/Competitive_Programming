'''
DCP #10

'''
import time
def func1():
	print("HELLO")
def func2():
	print("WORLD")
def schedule(t,n):
	time.sleep(n/1000)
	t()
schedule(func1,3000)
schedule(func2,4000)

