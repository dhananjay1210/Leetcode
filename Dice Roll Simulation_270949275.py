class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 1000000007
        dp = [[[0]*6 for i in range(16)] for j in range(n)]
        
        for k in range(6):
            dp[0][1][k] = 1
        
        for i in range(1,n):
            for k in range(6):
                for prev in range(6):
                    for j in range(1,min(rollMax[prev],i+1)+1):
                        if prev == k:
                            dp[i][j][k] += dp[i-1][j-1][prev]
                        else:
                            dp[i][1][k] += dp[i-1][j][prev]
                        dp[i][j][k] %= MOD
        return sum(dp[n-1][j][k] for k in range(6) for j in range(1,min(rollMax[k],n)+1))%MOD
        
        
