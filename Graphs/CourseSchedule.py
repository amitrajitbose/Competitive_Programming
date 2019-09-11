from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True
        
        dependencies = defaultdict(list)
        for i,j in prerequisites:
            dependencies[i].append(j)
        
        result = []
        visited, visiting = set([]), set([])

        def dfs(node):
            """
            Utility function for depth first search algorithm
            """
            if node in visited:
                return # base case

            visiting.add(node)
            for neighbour in dependencies[node]:
                if neighbour in visiting:
                    raise Exception('Cycle Found')

                if neighbour not in visited:
                    dfs(neighbour)
            
            visiting.remove(node)
            visited.add(node)
            result.append(node)

        for node in list(dependencies):
            try:
                dfs(node)
            except Exception as e:
                return False
        return True

# Algorithm: Topological Sort
# Time Complexity : O(V+E)
# V = Number of subjects / units
# E = Number of prerequisites / dependencies
# 207 LCM