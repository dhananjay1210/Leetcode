class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stc = []
        mx = 0
        for i in prices:
            while stc:
                ele = stc.pop()
                if ele<i:
                    mx = mx+ i-ele
            stc.append(i)
        return mx
