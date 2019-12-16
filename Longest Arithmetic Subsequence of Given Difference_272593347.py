class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {}
        k = difference
        for num in arr:
            if (num - k) in res:
                res[num] = res[num - k] + 1
            else:
                res[num] = 1
        return max(res.values())
