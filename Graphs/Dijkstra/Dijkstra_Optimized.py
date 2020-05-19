'''
This version of Dijkstra includes Min Heap or Priority Queue based implementation
Along with visited nodes counter and visit[] array to keep track of the visited nodes.
This saves some additional time by not revisiting the old nodes in the heap, which have been already optimised.
Once all nodes are visited, we break out of the loop. This also denotes that Dijkstra is a Greedy-like algorithm.

Note that, the previous implementation with Priority Queue, also works but we are adding optimised nodes in the heap
and popping them out, the old nodes still remain in the min heap and we have to pop them out to end the algorithm.
This has been improved in this implementation.

Problem Link : https://www.interviewbit.com/problems/dijsktra/
'''

import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    visited = 0
    visit = [False] * len(graph)
    while len(pq) > 0:
        if visited == len(graph):
            break
        # print (pq)
        current_distance, current_vertex = heapq.heappop(pq)
        if not visit[current_vertex]:
            visit[current_vertex] = True
            visited += 1
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if not visit[neighbor] and distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
    return distances
    
def getGraph(v, arr, directed=True):
    graph = {i:{} for i in range(v)}
    for i in range(len(arr)):
        graph[arr[i][0]][arr[i][1]] = arr[i][2]
        if not directed:
            graph[arr[i][1]][arr[i][0]] = arr[i][2] # undirected
    return graph
 
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        graph = getGraph(A,B,directed=False)
        table = calculate_distances(graph, C)
        return [table[i] if table[i]!=float('inf') else -1 for i in range(A)]

