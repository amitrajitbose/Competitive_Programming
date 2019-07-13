class Fibo(object):
    """docstring for Fibo"""
    def __init__(self):
        self.memo = []
        

    def fibonacci(self, n, debug=False):
        if debug:
            print(self.memo)
        if self.memo[n] != 0:
            return self.memo[n]
        if n==1 or n==2:
            self.memo[n] = 1
        else:
            self.memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.memo[n]

    def main(self, n):
        self.memo = [0 for i in range(n+1)]
        print(self.fibonacci(n))

Fibo().main(30)