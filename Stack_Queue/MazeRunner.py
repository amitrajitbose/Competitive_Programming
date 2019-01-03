'''
DCP #23

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the 
end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the 
minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall 
everywhere else on the second row.

Approach Used : Lee's Algorithm
'''

from pprint import pprint
class Solution(object):
	def __init__(self, maze, start, finish):
		self.maze = maze
		self.m = len(maze)
		self.n = len(maze[0])
		self.start = start
		self.finish = finish
		#CREATE VISITED MATRIX
		self.visited = [[False for i in range(self.n)]for j in range(self.m)]
		self.cost = [[-1 for i in range(self.n)]for j in range(self.m)]
		#MARK START POINT TO ZERO
		self.cost[start[0]][start[1]] = 0
		self.visited[start[0]][start[1]] = True
		self.queue = [] #PROCESS QUEUE

	def dimension(self):
		print("Grid Dimensions: ",self.m,"x",self.n)
	
	def isValid(self, x,y):
		if(x<0 or y<0 or x>=self.m or y>=self.n):
			return False
		elif(self.maze[x][y]=='t'):
			return False
		else:
			return True
	
	def printer(self, mat):
		for i in range(len(mat)):
			print(*mat[i])
		print("--------------")
	
	def go(self):
		if(len(self.queue)==0):
			return

		#self.printer(self.cost)
		x,y=self.queue[0][0],self.queue[0][1]
		self.queue.pop(0)

		if(not self.isValid(x,y)):
			return
		elif(x==self.finish[0] and y==self.finish[1]):
			return
		else:
			self.visited[x][y] = True
			# LEFT
			if(self.isValid(x,y-1) and not self.visited[x][y-1]):
				if(self.cost[x][y-1] == -1):
					self.cost[x][y-1] = self.cost[x][y] + 1
				else:
					self.cost[x][y-1] = min(self.cost[x][y] + 1, self.cost[x][y-1])
			# TOP
			if(self.isValid(x-1,y) and not self.visited[x-1][y]):
				if(self.cost[x-1][y] == -1):
					self.cost[x-1][y] = self.cost[x][y] + 1
				else:
					self.cost[x-1][y] = min(self.cost[x][y] + 1, self.cost[x-1][y])
			# RIGHT
			if(self.isValid(x,y+1) and not self.visited[x][y+1]):
				if(self.cost[x][y+1] == -1):
					self.cost[x][y+1] = self.cost[x][y] + 1
				else:
					self.cost[x][y+1] = min(self.cost[x][y] + 1, self.cost[x][y+1])
			# BOTTOM
			if(self.isValid(x+1,y) and not self.visited[x+1][y]):
				if(self.cost[x+1][y] == -1):
					self.cost[x+1][y] = self.cost[x][y] + 1
				else:
					self.cost[x+1][y] = min(self.cost[x][y] + 1, self.cost[x+1][y])
			
			#NOW GO AGAIN

			# LEFT
			if(self.isValid(x,y-1) and not self.visited[x][y-1]):
				self.queue.append((x,y-1))
			# TOP
			if(self.isValid(x-1,y) and not self.visited[x-1][y]):
				self.queue.append((x-1,y))
			# RIGHT
			if(self.isValid(x,y+1) and not self.visited[x][y+1]):
				self.queue.append((x,y+1))
			# BOTTOM
			if(self.isValid(x+1,y) and not self.visited[x+1][y]):
				self.queue.append((x+1,y))

			self.go()
			
	
	def minCost(self):
		self.queue.append((self.start[0], self.start[1]))
		self.go()
		return self.cost[self.finish[0]][self.finish[1]]
			


s = Solution([['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']], (3,0), (0,0))
print(s.minCost())
#print(s.cost)