# LC 1268
class TrieNode:
    def __init__(self):
        self.next = dict()
        self.words = list()
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            # node = node.next.setdefault(char, TrieNode())
            if char not in node.next:
                node.next[char] = TrieNode()
            node = node.next[char]
            if len(node.words) < 3:
                node.words.append(word)
    def getSuggestionsFor(self, word):
        ans = []
        node = self.root
        for char in word:
            if node:
                node = node.next.get(char, None)
            if node:
                ans.append(node.words)
            else:
                ans.append([])
        return ans
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.insert(word)
        return trie.getSuggestionsFor(searchWord)

