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
        dp = [[0 for i in range(n)] for j in range(2)]
        
        for k_ in range(1,k+1):
            temp = -prices[0]
            for i in range(1,n):
                dp[k_%2][i] = max(dp[k_%2][i-1],prices[i] + temp)
                temp = max(temp,dp[(k_-1)%2][i] - prices[i])
        return dp[k%2][n-1]
