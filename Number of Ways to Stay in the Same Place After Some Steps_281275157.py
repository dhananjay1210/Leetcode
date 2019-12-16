class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[-1 for i in range(501)] for j in range(501)]
        def rec(ptr,steps,arrLen):
            if steps == 0 and ptr == 0:
                    return 1
            if ptr<0 or ptr>=arrLen or steps == 0 or ptr > (steps):
                return 0
            if dp[ptr][steps] == -1:
                w1 = rec(ptr,steps-1,arrLen)
                w2 = rec(ptr+1,steps-1,arrLen)
                w3 = rec(ptr-1,steps-1,arrLen)
                
                dp[ptr][steps] = (w1 + w2 + w3) % 1000000007
            return dp[ptr][steps]
        rec(0,steps,arrLen)
        return dp[0][steps]
