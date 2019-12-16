class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        import bisect
        arr=[]
        for i in range(len(startTime)):
            arr.append([startTime[i], endTime[i], profit[i]])
        arr.sort(key=lambda x: x[1])
        dp = [[0, 0]]
        for start, end, prof in arr:
            ind = bisect.bisect(dp, [start+1]) - 1
            if dp[ind][1] + prof > dp[-1][1]:
                dp.append([end, dp[ind][1] + prof])
        return dp[-1][1]
