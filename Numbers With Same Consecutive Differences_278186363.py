class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        num = [0]*N
        final = []
        d = {}
        def rec(num,ind,k):
            if ind >= N:
                ans = 0
                p = 0
                for j in range(N-1,-1,-1):
                    ans += (num[j]* (10**p))
                    p += 1
                if ans not in d:
                    final.append(ans)
                    d[ans] = 1
                return
            
            if ind==0:
                for i in range(1,10):
                    num[0] = i
                    rec(num[:],ind+1,k)
            else:
                if num[ind-1] + k <=9:
                    num[ind] = num[ind-1] + k
                    rec(num[:],ind+1,k)
                if num[ind-1] - k >= 0:
                    num[ind] = num[ind-1] - k
                    rec(num[:],ind+1,k)
        rec(num,0,K)
        if N==1:
            final.append(0)
        return final
