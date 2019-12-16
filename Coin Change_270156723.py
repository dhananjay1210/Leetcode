class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        k,n = len(coins),amount        
        dp = [float("inf") for i in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = min(1+dp[i-c] if i-c>=0 else float("inf") for c in coins)
        if dp[n]==float("inf"):
            return -1
        return dp[n] 
