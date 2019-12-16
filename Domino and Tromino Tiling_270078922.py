class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 1000000007
        dp = [0 for i in range(N+1)]
        dp[0]=dp[1] = 1
        if N>1:
            dp[2] = 2
        if N>2:
            dp[3] = 5
        for i in range(4,N+1):
            dp[i] = (2*dp[i-1]+dp[i-3])%MOD
        return dp[N]
