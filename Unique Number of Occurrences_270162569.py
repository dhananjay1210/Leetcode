class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hs = {}
        for i in arr:
            if i in hs:
                hs[i] += 1
            else:
                hs[i] = 1
        hs2={}
        for k,v in hs.items():
            if v in hs2:
                return False
            else:
                hs2[v] = 1
        return True               
        
