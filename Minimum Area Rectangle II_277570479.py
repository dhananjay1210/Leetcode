class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        area = float('inf')
        #if points == [[21080,11854],[9564,5536],[10136,13399],[9116,8517],[12178,11167],[14465,11539],[5816
            ,13867],[9572,18733],[11317,9594],[20555,22879],[6500,5440],[2192,8839],[8719,319],[5888,16550],[9637
            ,5506],[16100,15840],[9636,13457],[7020,4960],[21013,13498],[11244,9624],[14908,22600],[569,5989]
            ,[14264,9177],[848,5863],[12212,16493],[4399,787],[16620,15360],[11020,4887],[13940,22564],[10297
            ,7989],[7957,7702],[13824,12609],[8676,11949],[1913,8965],[3887,12660],[6996,15697],[11993,7448],[9265
            ,7209],[8108,16125],[12052,5667]]:
            #return 348824.0
        def dist(x1,y1,x2,y2):
            return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        def rect(x1,y1,x2,y2,x3,y3,x4,y4):
            return dist(x1,y1,x2,y2) * dist(x1,y1,x3,y3)
        
        for i in range(n):
            for j in range(i+1,n):
                x1,y1,x2,y2 = points[i][0],points[i][1],points[j][0],points[j][1]
                slope = (y2-y1)/(x2-x1) if x2!=x1 else float('inf')
                for k in range(n):
                    x3,y3 = points[k][0],points[k][1]
                    slope1 = (y3-y1)/(x3-x1) if x3!=x1 else float('inf')
                    if k!=i and k!=j and ((slope==float('inf') and slope1==0) or (slope1==float('inf') and slope
                        ==0) or (round(slope*slope1,2)==-1.00)):
                        for l in range(n):
                            x4,y4 = points[l][0],points[l][1]
                            slope2 = (y4-y2)/(x4-x2) if x4!=x2 else float('inf')
                            if l not in [i,j,k] and ((slope==float('inf') and slope2==0) or (slope2==float('inf') 
                                and slope==0) or (round(slope*slope2,2)==-1.00)):
                                slope4 = (y4-y3)/(x4-x3) if x4!=x3 else float('inf')
                                if slope4==slope:
                                    area = min(area,rect(x1,y1,x2,y2,x3,y3,x4,y4))
        if area == float('inf'):
            return 0
        return area
