from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def reach(forest,curr_i,curr_j,dest_i,dest_j,rows,cols):
            level = 0
            q = deque()
            q.append([curr_i,curr_j,level])
            while q:
                ele = q.popleft()
                now_i,now_j,lvl = ele[0],ele[1],ele[2]
                forest[now_i][now_j] = 0

                if now_i == dest_i and now_j == dest_j:
                    return lvl

                for i,j in zip([1,-1,0,0],[0,0,1,-1]):
                    if 0<=now_i+i<rows and 0<=now_j+j<cols and forest[now_i+i][now_j+j] != 0:
                        q.append([now_i+i,now_j+j,lvl + 1])
                        forest[now_i+i][now_j+j] = 0
            return -1

        rows = len(forest)
        cols = len(forest[0]) if rows>0 else 0
        minus = 0
        if forest[0][0]>1:
            minus = 1
        sort_forest = [[forest[i][j],i,j] for i in range(rows) for j in range(cols)]
        sort_forest.sort()
        curr_i,curr_j = 0,0
        total_steps = 0
        #print(sort_forest)
        for i in range(len(sort_forest)):
            ele = sort_forest[i]
            if ele[0]!=0:
                temp = []
                for i in range(rows):
                    rw = []
                    for j in range(cols):
                        rw.append(forest[i][j])
                    temp.append(rw)
                steps = reach(temp,curr_i,curr_j,ele[1],ele[2],rows,cols)
                if steps != -1:
                    total_steps += steps
                else:
                    return -1
                curr_i,curr_j = ele[1],ele[2]
        return total_steps
