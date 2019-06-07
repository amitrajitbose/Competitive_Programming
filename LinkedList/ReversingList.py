class Node():
  """docstring for Node"""
  def __init__(self, val):
    super(Node, self).__init__()
    self.val = val
    self.next = None
    

def reverseLinkedList(head):
  prevn = None
  currn = head
  nextn = head.next
  head.next = None
  head = nextn
  while (nextn):
    prevn = currn
    currn = nextn
    nextn = head.next
    currn.next = prevn #reversing the link
    head = nextn
  return currn

def printlist(head):
  while head:
    print (head.val)
    head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
printlist(head)
head = reverseLinkedList(head)
print('-----')
printlist(head)