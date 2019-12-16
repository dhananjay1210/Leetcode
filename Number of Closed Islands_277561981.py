class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if 0<=i<n and 0<=j<m and grid[i][j] == 0:
                grid[i][j] = 1
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        n,m = len(grid),len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1) and grid[i][j] == 0:
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i,j)
                    ans += 1
        return ans
