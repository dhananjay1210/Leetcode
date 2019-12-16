class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        mx = len(A)
        n = len(A)
        ans = []
        while mx>0:
            pos = A.index(mx) + 1
            if pos != mx:
                ans.append(pos)
                temp = A[:pos-1]
                temp.reverse()
                A = temp + A[pos:]
                ans.append(mx)
                A = A[::-1]
            else:
                A = A[:mx-1]
            mx -= 1
        return ans
        
