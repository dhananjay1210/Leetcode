class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        from collections import Counter
        d = Counter(A)
        ans = 0
        if not A:
            return ans
        k = max(0,min(A))
        
        for ky in sorted(d.keys()):
            k = max(k,ky)
            while d[ky]>1:
                if k not in d:
                    d[k] = 1
                    d[ky] -= 1
                    ans += (k-ky)
                k += 1
        return ans
