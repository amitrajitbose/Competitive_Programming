class Node:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.next = {}
class Trie:
    def __init__(self):
        self.root = Node("")
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = Node(c)
            node = node.next[c]
        node.end = True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        self.seen = []

    def query(self, letter: str) -> bool:
        self.seen.append(letter)
        i = len(self.seen) - 1
        node = self.trie.root
        while i >= 0:
            node = node.next.get(self.seen[i], None)
            if not node:
                return False
            elif node.end:
                return True
            i -= 1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
