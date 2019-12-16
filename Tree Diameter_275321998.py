class Solution:
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.ans = -1
        if len(edges)==0:
            return 0
        d = {}
        mn,mx = 100000,-1
        for i,j in edges:
            mn = min(mn,i,j)
            mx = max(mx,i,j)
            if i in d:
                d[i].append(j)
            else:
                d[i] = [j]
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
                
        visited = [0]*(mx+1)
        #print(d)
        def dfs(node,visited):
            visited[node] = 1
            #print(visited)
            temp = []
            for i in d[node]:
                if not visited[i]:
                    ele = dfs(i,visited)
                    temp.append(ele)
            #print(node,temp)
            if temp:
                temp.sort()
                mx1,mx2 = 0,0
                mx1 = temp[-1]
                if len(temp)>1:
                    mx2 = temp[-2]
                self.ans = max(self.ans,mx1+mx2)
                visited[node] = 0
                return 1 + max(mx1,mx2)
            else:
                visited[node] = 0
                return 1
        dfs(edges[0][0],visited)
        return self.ans
