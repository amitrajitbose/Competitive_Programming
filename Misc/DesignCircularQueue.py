class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.arr = [-1] * k
        self.size = 0
        self.rear = -1
        self.front = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        if self.rear == -1 and self.front == -1:
            self.front += 1
        self.rear += 1
        self.rear %= self.capacity
        self.arr[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.arr[self.front] = -1
        self.front += 1
        self.front %= self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.arr[self.front]

    def Rear(self) -> int:
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
