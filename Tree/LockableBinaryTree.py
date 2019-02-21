'''
DCP #24

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded 
program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''

class LockableNode(object):
    """docstring for Lockable Binary Tree Node"""
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self._is_locked = False #by default a node is not locked
        self.locked_descendants = 0

    def is_locked(self):
        return self._is_locked

    def _can_lock_or_unlock(self):
        #check how many descendants are locked
        #if any descendant are locked
        #precaching this to reduce time complexity
        if(self.locked_descendants > 0):
            return False

        #check if any ancestors are locked
        curr = self.parent
        while(curr!=None):
            if(curr._is_locked):
                return False
            curr = curr.parent
        return True

    def lock(self):
        if(self._can_lock_or_unlock):
            #not locked
            self._is_locked = True
            #increment count in all ancestors
            curr = self.parent
            while(curr!=None):
                curr.locked_descendants += 1
                curr = curr.parent
            return True
        return False

    def unlock(self):
        if(self._can_lock_or_unlock):
            #can unlock
            self._is_locked = False

            #decrement count in all ancestor
            curr = self.parent
            while (curr!=None):
                curr.locked_descendants -= 1
                curr = curr.parent
            return True
        return False

def main():
    print("Implementation not necessary..")