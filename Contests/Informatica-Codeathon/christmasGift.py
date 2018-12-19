#! /usr/bin/python3
from collections import defaultdict


class Graph:

    def __init__(self, n):
        ''' using default dict to store edges & weights of initialized graph'''
        self.graph = defaultdict(dict)
        self.gifts = [0]*n

    def addEdge(self, u, v, weight=1):
        ''' adding edges u->v with weight or 1 otherwise '''
        self.graph[u][v] = weight

    def addGift(self, src, des, parent):
        crawl = des
        self.gifts[crawl] += 1
        while parent[crawl] != -1:
            self.gifts[parent[crawl]] += 1
            crawl = parent[crawl]

    def traverse(self, src, des, vertex):
        ''' taverse from i to j adding 1 to all visited nodes '''
        ''' bfs traversal from vertex s '''
        visited = [False]*(vertex)  # to keep track of visted vertices
        queue = []  # data structure to hold visted vertex in FIFO fashion & acheive BFS
        parent = [-1] * (vertex)   # to track the order of visit
        queue.append(src)
        visited[src] = True

        while queue:
            s = queue.pop(0)

            for vertices in self.graph[s]:
                if not visited[vertices]:
                    queue.append(vertices)
                    visited[vertices] = True
                    parent[vertices] = s
                    if vertices == des:
                        self.addGift(src, des, parent)
                        return True  # found dest
        return False


if __name__ == "__main__":

    # print("Enter no. of cities and days of visit")
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    g = Graph(n)
    # print("Enter routes u->v:w\n"%m)directed graph ,add two edges for undirec
    for edges_i in range(n-1):
        u, v = [int(edges_temp) for edges_temp in input().strip().split(' ')]
        g.addEdge(u-1, v-1)
        g.addEdge(v-1, u-1)

    for days in range(m):
        i, j = [int(start_finish) for start_finish in input().split(' ')]
        g.traverse(i-1, j-1, n)

    print(max(g.gifts))