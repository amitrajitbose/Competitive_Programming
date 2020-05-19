# LC 743

import heapq
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        # print (pq)
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
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
        dist = [distMap[i] for i in range(N)]
        if float('inf') in dist:
            return -1
        else:
            return max(dist)

