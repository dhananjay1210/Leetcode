class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        hs = [1]*(maxChoosableInteger+1)
        hs[0] = 0
        if desiredTotal==0:
            return True
        if desiredTotal > (maxChoosableInteger *(maxChoosableInteger+1)/2):
            return False
        dp = {}
        
        def rec(hs,n,total,dp):
            if total<=0:
                return True
            if str(hs) not in dp:
                win = False
                for i in range(1,n):
                    if hs[i]:
                        hs[i] = 0
                        win = win or rec(hs,n,total-i,dp)
                        hs[i] = 1
                        if win:
                            break
                dp[str(hs)] = not win
            return dp[str(hs)]
        
        res = not rec(hs,maxChoosableInteger+1,desiredTotal,dp)
        #print(dp)
        return res
