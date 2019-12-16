class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stc = []
        mx = 0
        for i in prices:
            while stc and stc[-1]>=i:
                ele = stc.pop()
                if stc:
                    mx = max(mx,ele-stc[0])
            stc.append(i)
        while stc:
            ele = stc.pop()
            if stc:
                mx = max(mx,ele-stc[0])
        return mx
