class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        uf = {}
        size = {}
        n = len(grid)
        def find(x):
            uf.setdefault(x,x)
            size.setdefault(x,1)
            if x != uf[x]:
                uf[x] = uf[uf[x]]
                return find(uf[x])
            return x
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if size[px] <= size[py]:
                uf[px] = py
                size[py] += size[px]
            else:
                uf[py] = px
                size[px] += size[py]
        
        for i in range(n):
            for j in range(n):
                if i:
                    union((i,j,0),(i-1,j,2))
                if j:
                    union((i,j,3),(i,j-1,1))
                if grid[i][j] != '/':
                    union((i,j,0),(i,j,1))
                    union((i,j,2),(i,j,3))
                if grid[i][j] != "\\":
                    union((i,j,0),(i,j,3))
                    union((i,j,1),(i,j,2))
        res= 0
        for x in uf:
            if x == uf[x]:
                res+=1
        return res
