class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        mx,mx_i,mx_j = 1,0,0
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if s[i]==s[j] and dp[i+1][j-1] !=0:
                    dp[i][j] = (2 if dp[i+1][j-1]==-1 else dp[i+1][j-1] + 2)
                else:
                    dp[i][j] = 0
                
                if mx<dp[i][j]:
                    mx,mx_i,mx_j = dp[i][j],i,j
        #print(mx,mx_i,mx_j)
        return s[mx_i:mx_j+1]
