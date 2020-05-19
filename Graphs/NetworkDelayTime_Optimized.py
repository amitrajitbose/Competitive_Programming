# LC743
# Optimized with visited array and algorithm termination once all nodes are visited

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
        graph[arr[i][0]-1][arr[i][1]-1] = arr[i][2]
        if not directed:
            graph[arr[i][1]-1][arr[i][0]-1] = arr[i][2] # undirected
    return graph

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = getGraph(N, times)
        distMap = calculate_distances(graph, K-1)
        dist = []
        maxm = -float('inf')
        for i in range(N):
            edgeWt = distMap[i]
            if edgeWt == float('inf'):
                return -1
            dist.append(edgeWt)
            maxm = max(maxm, edgeWt)
        return maxm

