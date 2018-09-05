'''
Kruskal's Algorithm for Minimum Spanning Tree
Author: Amitrajit Bose
Approach : Greedy
Aim: To calculate minimum cost spanning tree

Problem: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
'''

def findSet(vertex, connected):
	return connected[vertex]

def union(connected,v,v1,v2):
	for i in range(v+1):
		if(connected[i]==v2):
			connected[i]=v1
	return connected

def kruskal(graph, v):
	#graph is a set of tuples of edges
	#define the null set A that will contain marked/visited vertices
	mstEdgeSet=[]
	mstVertexSet=[]
	totalWeight=0
	connected=[]
	#initialising connected
	for i in range(v+1):
		connected.append(i)

	#sort the tuples in the graph w.r.t their edges
	graph=sorted(graph, key=lambda x: x[2])
	totalEdges = v-1
	for e in graph:
		if(totalEdges==0):
			break
		v1=findSet(e[0],connected)
		v2=findSet(e[1],connected)
		if(v1 != v2):
			#so we append the edge to mst edge set
			mstEdgeSet.append(e)
			totalWeight += e[2]
			totalEdges -= 1
			mstVertexSet.append(e[1])
			connected = union(connected, v, v1, v2)
	return (totalWeight, mstEdgeSet)

def main():
	v,e=[int(x) for x in input().strip().split()]
	graph=[]
	for _ in range(e):
		edge = [int(x) for x in input().strip().split()]
		graph.append(edge)
	#calling kruskal now
	k=kruskal(graph, v)
	print(k[0])


if __name__=='__main__':
	main()

