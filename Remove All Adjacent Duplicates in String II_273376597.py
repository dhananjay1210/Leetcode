class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stc = []
        for i in s:
            if stc and stc[-1][0] == i:
                stc.append([i,stc[-1][1]+1])
            else:
                stc.append([i,1])
            if stc[-1][1]==k:
                temp = k
                while(temp):
                    stc.pop()
                    temp-=1
        return "".join([k[0] for k in stc])
