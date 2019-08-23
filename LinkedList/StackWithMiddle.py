"""
How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

Also add a print() operation which works in linear time
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return "[" + str(self.data) + "] -> "

class Stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def size(self):
        return self.count

    def push(self, data):
        newNode = Node(data)
        if not self.head or self.size() == 0:
            # first push
            self.head = newNode
            self.count += 1
            self.mid = self.head
        else:
            self.count += 1
            oldHead = self.head
            self.head = newNode
            newNode.prev = oldHead
            oldHead.next = newNode

            if self.size() % 2:
                self.mid = self.mid.next # if odd, mid = mid->next

    def pop(self):
        if not self.head or self.size() == 0:
            print("STACK UNDERFLOW")
        else:
            oldHead = self.head
            popped = oldHead.data
            self.head = oldHead.prev
            self.head.next = None
            del oldHead # free up memory
            self.count -= 1

            if self.size() % 2 == 0:
                self.mid = self.mid.prev # if even, mid = mid->prev
            return popped

    def findMiddle(self):
        return self.mid.data

    def deleteMiddle(self):
        oldMid = self.mid
        popped = oldMid.data
        pre = oldMid.prev
        nxt = oldMid.next
        pre.next = nxt
        nxt.prev = pre
        del oldMid
        self.count -= 1

        if self.size() % 2:
            self.mid = nxt
        else:
            self.mid = pre

        return popped

    def print(self):
        if self.size() == 0:
            print("EMPTY")
        else:
            ptr = self.head
            while ptr:
                print(ptr, end = '')
                ptr = ptr.prev
            print("[x]")

st = Stack()
st.push(1)
st.push(2)
st.print()
st.push(3)
st.print()
print("Mid",st.findMiddle())
st.pop()
st.print()
st.push(3)
st.push(4)
st.print()
st.deleteMiddle()
st.print()
st.deleteMiddle()
st.print()

"""
OUTPUT
------

[2] -> [1] -> [x]
[3] -> [2] -> [1] -> [x]
Mid 2
[2] -> [1] -> [x]
[4] -> [3] -> [2] -> [1] -> [x]
[4] -> [3] -> [1] -> [x]
[4] -> [1] -> [x]
"""

