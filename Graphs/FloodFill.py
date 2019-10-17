# LCE733
class Solution:
    
    def __init__(self):
        self.image = []
    
    def isValid(self, image: List[List[int]], i: int, j: int) -> bool:
        if i<0 or j<0:
            return False
        if i>=len(image):
            return False
        if j>=len(image[i]):
            return False
        return True
        
    def floodFillUtil(self, image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int):
        if not self.isValid(self.image, sr, sc):
            return # not a valid pixel location
        if self.image[sr][sc]==newColor or self.image[sr][sc]!=oldColor:
            return # no work to be done on this pixel
        else:
            self.image[sr][sc] = newColor
            self.floodFillUtil(self.image, sr, sc+1, oldColor, newColor)
            self.floodFillUtil(self.image, sr, sc-1, oldColor, newColor)
            self.floodFillUtil(self.image, sr+1, sc, oldColor, newColor)
            self.floodFillUtil(self.image, sr-1, sc, oldColor, newColor)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.floodFillUtil(self.image, sr, sc, image[sr][sc], newColor)
        return self.image
        
