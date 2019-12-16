class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        import collections
        cnt,freq = collections.defaultdict(int), collections.defaultdict(int)
        res,maxF = 0,0
        n = len(nums)
        for j in range(n):
            num = nums[j] 
            cnt[num] = cnt.get(num,0) + 1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] = freq.get(cnt[num],0) + 1
            maxF = max(maxF,cnt[num])
            if maxF*freq[maxF] == j or (maxF-1)*(freq[maxF-1]+1) == j or maxF == 1:
                res = j + 1
        return res
