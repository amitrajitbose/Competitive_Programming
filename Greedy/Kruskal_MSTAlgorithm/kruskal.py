'''
Kruskal's Algorithm Approach
Author: Amitrajit Bose
Approach : Greedy
Aim: To calculate minimum cost spanning tree
'''

def findSet(vertex, A):
	if(vertex in A):
		return True
	else:
		return False
def kruskal(graph, v):
	#graph is a set of tuples of edges
	#define the null set A that will contain marked/visited vertices
	mstEdgeSet=[]
	mstVertexSet=[]
	totalWeight=0

	#sort the tuples in the graph w.r.t their edges
	graph=sorted(graph, key=lambda x: x[2])
	#print(graph)
	totalEdges = v-1
	mstVertexSet.append(graph[0][0]) #adding the first node by default
	for e in graph:
		if(totalEdges==0):
			break
		if((findSet(e[0],mstVertexSet) != findSet(e[1],mstVertexSet))or(findSet(e[0],mstVertexSet)==False and findSet(e[1],mstVertexSet)==False)):
			#so we append the edge to mst edge set
			mstEdgeSet.append(e)
			totalWeight += e[2]
			totalEdges -= 1
			mstVertexSet.append(e[1])
	return (totalWeight, mstEdgeSet)

def main():
	v=int(input("Enter Total Number Of Vertices: "))
	e=int(input("Enter Total Number Of Edges: "))
	print("Enter Source Vertex<space>Destination Vertex<space>Edge Weight")
	graph=[]
	for _ in range(e):
		edge = [int(x) for x in input().strip().split()]
		graph.append(edge)
	#call kruskal now
	k=kruskal(graph, v)
	#print("\n",k[1],"\n")
	print("Total MST Weight: ",k[0])
	print("\nResultant Minimum Spanning Tree")
	print("Src\tDestn\tWeigh")
	for i in k[1]:
		print(" {0}\t  {1}\t  {2}".format(i[0],i[1],i[2]))

if __name__=='__main__':
	main()

