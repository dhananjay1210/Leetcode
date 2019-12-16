class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n==0:
            return 0
        if k>=n//2:
            sm = 0
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    sm += prices[i]-prices[i-1]
            return sm
        dp = [[0 for i in range(n)] for j in range(k+1)]
        
        for k_ in range(1,k+1):
            temp = -prices[0]
            for i in range(1,n):
                dp[k_][i] = max(dp[k_][i-1],prices[i] + temp)
                temp = max(temp,dp[k_-1][i] - prices[i])
        return dp[k][n-1]
