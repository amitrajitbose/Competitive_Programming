#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    
    def addEdge(self, a,b):
        self.adj[a].append(b)
        self.adj[b].append(a)
    
    def dfs_util(self, temp, node, visited):
        visited[node] = True
        temp.append(node)
        for i in self.adj[node]:
            if not visited[i]:
                temp = self.dfs_util(temp, i, visited)
        return temp
    
    def countGroups(self):
        """
        This is the classical concept of connected components in a Graph
        """
        visited = [False] * self.V
        groups = []
        for node in range(self.V):
            if not visited[node]:
                temp = []
                groups.append(self.dfs_util(temp, node, visited))
        return groups

def convertMatrixToGraph(mat):
    """
    Accept the input which is an adjacency matrix and return a Graph, which is an adjacency list
    """
    n = len(mat)
    g = Graph(n)
    for i in range(n):
        for j in range(n):
            if j > i and mat[i][j] == '1':
                g.addEdge(i,j)
    return g

def countGroups(related):
    # Write your code here
    graph = convertMatrixToGraph(related)
    groups = graph.countGroups()
    # print(groups)
    return len(groups)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)

    result = countGroups(related)

    fptr.write(str(result) + '\n')

    fptr.close()
