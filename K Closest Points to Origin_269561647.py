class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from heapq import heappush,heappop
        minHeap = []
        for p in points:
            heappush(minHeap,[p[0]**2 + p[1]**2,p[0],p[1]])
        res = []
        while K:
            cost,x,y = heappop(minHeap)
            res.append([x,y])
            K-=1
        return res
        
