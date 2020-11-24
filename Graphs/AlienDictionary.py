class Solution:
    def getTopoOrder(self, graph):
        res = [] # stack for topological sort
        visited,visiting = set([]), set([])
        def dfs(node):
            if node in visited:
                return
            visiting.add(node)
            for n in graph[node]:
                if n in visiting:
                    raise Exception("Cycle")
                if n not in visited:
                    dfs(n)
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            
        for node in graph:
            try:
                dfs(node)
            except Exception as ex:
                return []
        return res
        
    def alienOrder(self, words: List[str]) -> str:
        graph = {c : [] for word in words for c in word}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    graph[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""
        return ''.join(self.getTopoOrder(graph))
