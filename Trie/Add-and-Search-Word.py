class TrieNode:
    def __init__(self):
        self.edges = dict()

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode() # dummy root node

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            node = node.edges.setdefault(c, TrieNode())
        node.edges['$'] = TrieNode() # $ marks the end of a word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchUtil(word, self.trie)
    
    def searchUtil(self, word, node):
        for i in range(len(word)):
            ch = word[i]
            if ch in node.edges:
                node = node.edges[ch] # if not a wildcard & next char is present
            elif ch != '.':
                return False # no such valid word present
            elif ch == '.':
                # iterate over all edges and recurse
                for key in node.edges:
                    if self.searchUtil(word[i+1 : ], node.edges[key]):
                        return True
                return False
        return '$' in node.edges # if the word has proper ending, if it word exists
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
