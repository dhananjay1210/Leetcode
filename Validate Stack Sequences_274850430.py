class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stc = []
        i,j = 0,0
        while i<len(pushed):
            while stc and j<len(popped) and stc[-1]==popped[j]:
                stc.pop()
                j+=1
            stc.append(pushed[i])
            i+=1
        while stc and j<len(popped) and stc[-1]==popped[j]:
            stc.pop()
            j+=1
        if stc:
            return False
        else:
            return True
