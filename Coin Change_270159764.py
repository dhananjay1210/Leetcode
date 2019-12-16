class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        def rec(dp,coins,amt):
            if amt<0:
                return -1
            if amt==0:
                return 0
            if dp[amt]==-1:
                mn = float("inf")
                for c in coins:
                    ret = rec(dp,coins,amt-c)
                    mn = min(mn,1+ret if ret>=0 else float("inf"))
                dp[amt] = mn
            return dp[amt]
        rec(dp,coins,amount)
        if dp[amount]==float("inf"):
            return -1
        return dp[amount]
