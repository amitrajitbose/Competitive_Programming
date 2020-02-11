class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []
        self.min = -1
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.stack) == 1 or x <= self.min:
            self.mins.append(x)
            self.min = x

    # @return nothing
    def pop(self):
        if not len(self.stack):
            return -1
        if self.stack[-1] == self.min:
            self.mins.pop(-1)
            self.min = self.mins[-1] if len(self.mins)>0 else -1
        self.stack.pop(-1)
        

    # @return an integer
    def top(self):
        return self.stack[-1] if len(self.stack) else -1
        

    # @return an integer
    def getMin(self):
        return self.min

