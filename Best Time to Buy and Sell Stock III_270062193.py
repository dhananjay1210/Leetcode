class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k,n = 2,len(prices)
        if n==0:
            return 0
        dp = [[0 for i in range(n)] for j in range(k+1)]
        
        for i in range(1,k+1):
            temp = dp[i-1][0] - prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1],prices[j] + temp)
                temp = max(temp,dp[i-1][j] - prices[j])
        #print(dp)
        return dp[k][n-1]
