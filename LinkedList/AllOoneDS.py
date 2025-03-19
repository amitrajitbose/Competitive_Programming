# LC 432 -> https://leetcode.com/problems/all-oone-data-structure/
class LLNode:
    # doubly linked list node
    def __init__(self, count):
        self.count = count
        self.keys = set([])
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.keyToCount = {}
        self.countToNode = {}
        self.head = LLNode('head')
        self.tail = LLNode('tail')
        # initialise
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def printDLL(self):
        i = self.head
        res = []
        while i != self.tail:
            res.append("{}-({})".format(i.count, i.keys))
            i = i.next
        print("DLL:{}".format(res))

    def _addAfter(self, newNode, prevNode):
        # print("Adding node {} after {}...".format(newNode.count, prevNode.count))
        newNode.next = prevNode.next
        newNode.prev = prevNode
        prevNode.next.prev = newNode
        prevNode.next = newNode
        # print(self.countToNode)
    
    def _removeNode(self, node):
        # print("Removing node {}...".format(node.count))
        node.prev.next = node.next
        node.next.prev = node.prev
        # print(self.countToNode)

    def inc(self, key: str) -> None:
        if key in self.keyToCount:
            prevCount = self.keyToCount[key]
            newCount = prevCount + 1
            self.keyToCount[key] = newCount

            currNode = self.countToNode[prevCount]
            currNode.keys.remove(key)

            if len(currNode.keys) == 0:
                del self.countToNode[prevCount]
                self._removeNode(currNode)
            
            if newCount not in self.countToNode:
                newNode = LLNode(newCount)
                self.countToNode[newCount] = newNode
                if prevCount in self.countToNode:
                    self._addAfter(newNode, currNode)
                else:
                    self._addAfter(newNode, currNode.prev)
            self.countToNode[newCount].keys.add(key)
        else:
            self.keyToCount[key] = 1
            if 1 not in self.countToNode:
                newNode = LLNode(1)
                self.countToNode[1] = newNode
                self._addAfter(newNode, self.head)
            self.countToNode[1].keys.add(key)
        # self.printDLL()


    def dec(self, key: str) -> None:
        if key not in self.keyToCount:
            print("Weird, this should not happen as per guarantee")
            return
        prevCount = self.keyToCount[key]
        currNode = self.countToNode[prevCount]
        currNode.keys.remove(key)
        if len(currNode.keys) == 0:
            del self.countToNode[prevCount]
            self._removeNode(currNode)
        if prevCount == 1:
            del self.keyToCount[key]
        else:
            newCount = prevCount - 1
            self.keyToCount[key] = newCount
            if newCount not in self.countToNode:
                newNode = LLNode(newCount)
                self.countToNode[newCount] = newNode
                self._addAfter(newNode, currNode.prev)
            self.countToNode[newCount].keys.add(key)
        # self.printDLL() 

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        res = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(res)
        return res

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        res = self.head.next.keys.pop()
        self.head.next.keys.add(res)
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
