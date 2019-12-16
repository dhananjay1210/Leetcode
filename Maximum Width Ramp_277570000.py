class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        left_min = [0]*n
        right_max = [0]*n

        left_min[0] = A[0]
        for i in range(1,n):
            left_min[i] = min(A[i],left_min[i-1])
        right_max[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(A[i],right_max[i+1])
            
        i=j=0
        mx = -1
        while i<n and j<n:
            if left_min[i]<=right_max[j]:
                mx = max(mx,j-i)
                j+=1
            else:
                i+=1
        return mx
