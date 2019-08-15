# LRU Cache - LeetCode: https://leetcode.com/problems/lru-cache/
# Author: Amitrajit Bose
# Date : August 15th, 2019

class Node:
    """
    Structure of a node in the doubly linked list
    """
    def __init__(self, key: int, data: int):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {} # key = int, value = Node
        # Dummy Nodes
        self.head = Node(None, None)
        self.head.prev = None
        self.tail = Node(None, None)
        self.tail.next = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Access an item from the cache
        """
        if len(self.hmap) == 0 or key not in self.hmap:
            return -1
        this_node = self.hmap[key]
        self.moveToHead(this_node)
        return this_node.data

    def put(self, key: int, value: int) -> None:
        """
        Add or Update an item in the cache
        """
        if key in self.hmap:
            this_node = self.hmap[key]
            this_node.data = value
            self.moveToHead(this_node)
        else:
            new_node = Node(key, value)
            self.hmap[key] = new_node
            self.addFirst(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                self.removeLRUEntry()    
    
    def removeLRUEntry(self):
        """
        Evicts the least recently used item from cache
        """
        tail_node = self.popTail()
        del self.hmap[tail_node.key]
        self.size -= 1

    def addFirst(self, node):
        """
        Adds a node at the beginning of the linked list
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        """
        Removes a node from the doubly linked list
        """
        oldprev, oldnext = node.prev, node.next
        oldprev.next = oldnext
        oldnext.prev = oldprev

    def moveToHead(self, node):
        """
        Removes the node and puts it at the beginning of the cache (list)
        """
        self.removeNode(node)
        self.addFirst(node)

    def popTail(self):
        """
        Removes and returns the element pointed by the tail of the list
        """
        rem = self.tail.prev
        self.removeNode(rem)
        return rem

    def display(self):
        """
        Prints the elements in the cache in order
        """
        p = self.head.next
        while p.next:
            print("[Key:{0}, Value:{1}]".format(p.key,p.data), end=" ")
            p = p.next
        print("")
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)