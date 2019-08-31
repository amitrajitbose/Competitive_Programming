
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None 
        self.height = 1

def rotateRight(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def rotateLeft(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def max(a, b):
    if a > b:
        return a
    else:
        return b

def Balance(current):
    if current == None:
        return 0
    return (height(current.left) - height(current.right))

def height(current):
    if current == None:
        return 0
    return current.height

def makeRoot(key):
    return Node(key)

def insert(current, key):
    if current == None:
       return Node(key)
    if key < current.key:
        current.left = insert(current.left, key)
    else:
        current.right = insert(current.right, key)
    current.height = max(height(current.left), height(current.right)) + 1
    balance = Balance(current)
    #left left
    if balance > 1 and key < current.left.key:
        return rotateRight(current)
    #right right
    if balance < -1 and key > current.right.key:
       return rotateLeft(current)
    #left right
    if balance > 1 and key > current.left.key:
        current.left =  rotateLeft(current.left);
        return rotateRight(current)
    #right left
    if balance < -1 and key < current.right.key:
        current.right = rotateRight(current.right);
        return rotateLeft(current);
    
    return current
    
def preOrder(temp):
    if temp != None:
        print (temp.key, " ", temp.height, " ", Balance(temp))
        preOrder(temp.left)
        preOrder(temp.right)

def main():
    root = makeRoot(10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)
    #for x in range(0, 5):
        #root = insert(root, random.randint(0,100))
    print (root.key)
    preOrder(root)
   
if __name__ == "__main__":
    main()
