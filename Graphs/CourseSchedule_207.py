class Graph:
    def __init__(self, nodes):
        self.node = {i: set([]) for i in range(nodes)}
    def addEdge(self, src, dest, dir=False):
        self.node[src].add(dest)
        if not dir:
            self.node[dest].add(src) # for undirected edges

class Solution:
    def hasCycle(self, graph):
        whiteset = set(graph.node.keys())
        grayset = set([])
        blackset = set([])
        while len(whiteset) > 0:
            curr = whiteset.pop()
            if self.dfs(curr, graph, whiteset, grayset, blackset):
                return True
        return False
    def dfs(self, curr, graph, whiteset, grayset, blackset):
        if curr in whiteset:
            whiteset.remove(curr)
        grayset.add(curr)
        for neighbor in graph.node[curr]:
            if neighbor in blackset:
                continue #already explored
            if neighbor in grayset:
                return True  #cycle found
            if self.dfs(neighbor, graph, whiteset, grayset, blackset):
                return True
        grayset.remove(curr)
        blackset.add(curr)
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses)
        for src, dest in prerequisites:
            g.addEdge(src, dest, dir=True)
        return not self.hasCycle(g)

