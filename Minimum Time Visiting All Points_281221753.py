class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            diffx = abs(p2[0] - p1[0])
            diffy = abs(p2[1] - p1[1])
            if diffx < diffy:
                cnt += diffx
                cnt += (diffy - diffx)
            else:
                cnt += diffy
                cnt += (diffx - diffy)
        return cnt
