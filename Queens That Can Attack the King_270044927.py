class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        chess = [[0 for i in range(8)] for j in range(8)]
        for i in queens:
            chess[i[0]][i[1]] = 1
        direct = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        res = []
        
        x,y = king[0],king[1]
        for di_x,di_y in direct:
            temp_x,temp_y = x,y
            while 0<=temp_x<8 and 0<=temp_y<8 and chess[temp_x][temp_y]==0:
                temp_x += di_x
                temp_y += di_y
            if 0<=temp_x<8 and 0<=temp_y<8 and chess[temp_x][temp_y]:
                res.append([temp_x,temp_y])
        return res
