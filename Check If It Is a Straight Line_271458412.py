class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        pts = coordinates
        n = len(pts)
        if pts[0][0] == pts[1][0]:
            for i in range(2,n):
                if pts[i][0] != pts[0][0]:
                    return False
            return True
        else:
            slope = (pts[1][1]-pts[0][1]) / (pts[1][0]-pts[0][0])
            for i in range(2,n):
                if slope != (pts[i][1]-pts[0][1]) / (pts[i][0]-pts[0][0]):
                    return False
            return True
