class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        count = 0
        r = [0 for i in range(n)]
        c = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (r[i]>1 or c[j]>1):
                    count += 1
        return count
