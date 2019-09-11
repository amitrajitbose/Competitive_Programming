class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        dependencies = {}
        
        # Initializing the graph, adding only nodes
        for i in range(numCourses):
            dependencies[i] = []
        
        # Adding the edges
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
                return []
        return result

# Algorithm: Topological Sort
# Time Complexity : O(V+E)
# V = Number of subjects / units
# E = Number of prerequisites / dependencies
# 210 LCM