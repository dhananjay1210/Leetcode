class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def rec(arr,ind,s):
            if ind>=len(arr):
                return 0
            mx1,mx2 = 0,0
            if len(set(arr[ind])) == len(arr[ind]):
                if len(s.intersection(arr[ind])) == 0:
                    uni = s.union(arr[ind])
                    mx1 = len(arr[ind]) + rec(arr,ind+1,uni)
            mx2 = rec(arr,ind+1,s)
            return max(mx1,mx2)
        return rec(arr,0,set())        
