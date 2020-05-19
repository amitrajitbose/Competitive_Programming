# PRIORITY QUEUE BASED IMPLEMENTATION OF DIJKSTRA ALGO
# TIME : O(E log V)
# Problem Link : https://www.interviewbit.com/problems/dijsktra/

import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    visit = [False for vertex in graph]
    visit[starting_vertex] = True
    while len(pq) > 0:
        # print (pq)
        current_distance, current_vertex = heapq.heappop(pq)
        visit[current_vertex] = True
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Only consider this new path if it's better than any path we've already found.
            if not visit[neighbor] and distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return sorted(distances.items())
    
def getGraph(v, arr):
    graph = {i:{} for i in range(v)}
    for i in range(len(arr)):
        graph[arr[i][0]][arr[i][1]] = arr[i][2]
        graph[arr[i][1]][arr[i][0]] = arr[i][2] # undirected
    return graph

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        graph = getGraph(A,B)
        return [i[1] if i[1]!=float('inf') else -1 for i in calculate_distances(graph, C)]
