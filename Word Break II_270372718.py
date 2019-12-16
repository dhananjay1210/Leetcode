class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        def rec(s,d,start,dp):
            n = len(s)
            if start>=n:
                return [""]

            ans = []
            if start not in dp:
                for i in range(start,n+1):
                    if s[start:i] in d:
                        list_ = rec(s,d,i,dp)
                        poss = [s[start:i] + " " + j for j in list_]
                        
                        ans+=(poss)
                dp[start] = ans
            return dp[start]

        rec(s,set(wordDict),0,dp)
        for i in range(len(dp[0])):
            dp[0][i] = dp[0][i].strip()
        return dp[0]
