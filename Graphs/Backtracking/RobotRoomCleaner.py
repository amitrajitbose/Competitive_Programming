# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
        
class Solution:
    def cleanRoom(self, robot):
        self.search_and_clean(robot, 0, 0, set())
            
            
    def search_and_clean(self, robot, i, j, visited):
        if (i, j) in visited: 
            return False
        visited.add((i,j))
        robot.clean()
        
        if self.go_left(robot):
            self.search_and_clean(robot, i, j-1, visited)
            self.go_right(robot)
        
        if self.go_right(robot):
            self.search_and_clean(robot, i, j+1, visited)
            self.go_left(robot)
        
        if self.go_down(robot):
            self.search_and_clean(robot, i+1, j, visited)
            self.go_up(robot)
        
        if self.go_up(robot):
            self.search_and_clean(robot, i-1, j, visited)
            self.go_down(robot)
        
    def go_left(self, robot):
        robot.turnLeft()
        left = robot.move()
        robot.turnRight()
        return left
        
    def go_right(self, robot):
        robot.turnRight()
        right = robot.move()
        robot.turnLeft()
        return right
    
    def go_down(self, robot):
        robot.turnRight()
        robot.turnRight()
        down = robot.move()
        robot.turnLeft()
        robot.turnLeft()
        return down
        
    def go_up(self, robot):
        return robot.move()
