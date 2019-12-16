class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        from collections import Counter
        def atmostK(A,K):
            cnt=j=0
            d = Counter()
            for i in range(len(A)):
                if d[A[i]]==0:
                    K-=1
                d[A[i]] += 1
                while K<0:
                    d[A[j]] -= 1
                    if d[A[j]]==0:
                        K+=1
                    j += 1
                cnt += (i-j+1)
            return cnt
        return atmostK(A,K) - atmostK(A,K-1)
