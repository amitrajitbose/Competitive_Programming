'''
DCP #10

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
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

