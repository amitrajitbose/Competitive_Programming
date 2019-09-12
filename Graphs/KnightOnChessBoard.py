"""
Minimum moves needed by knight to go from source to destination. If not possible
return -1

The first argument of input contains an integer A.
The second argument of input contains an integer B.
    => The chessboard is of size A x B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
    => The Knight is initially at position (C, D).
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.
    => The Knight wants to reach position (E, F).
"""

class Point:
    def __init__(self, x, y, distance = 0):
        self.x = x
        self.y = y
        self.distance = distance

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer

    def knight(self, A, B, C, D, E, F):
        
        def isValid(x, y):
            # check if (x,y) is a valid move
            if x>=1 and x<=A and y>=1 and y<=B:
                return True
            return False
            
        def minimumSteps(curr, dest):
            
            movex = [2,2,-2,-2,1,-1,1,-1]
            movey = [1,-1,1,-1,2,2,-2,-2]
            
            queue = [] # used for BFS
            queue.append(Point(curr[0],curr[1]))
            
            visited = [[False for i in range(B+1)] for j in range(A+1)]
            
            # mark current position as visited
            visited[curr[0]][curr[1]] = True
            
            while(len(queue)):
                
                # we process or keep visiting
                target = queue.pop(0)
                
                # so we need a base case
                if target.x==dest[0] and target.y==dest[1]:
                    return target.distance
                    
                # check as other possibilities
                for i in range(8):
                    x = target.x + movex[i]
                    y = target.y + movey[i]
                    if (isValid(x,y) and not visited[x][y]):
                        visited[x][y] = True
                        queue.append(Point(x,y,target.distance+1))
        
        curr = [C, D]
        dest = [E, F]
        x = minimumSteps(curr, dest)
        if x == None:
            return -1
        else:
            return x
