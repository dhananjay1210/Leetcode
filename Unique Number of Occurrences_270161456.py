class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hs = {}
        for i in arr:
            hs[i] = 1 + hs.get(i,0)
        hs2={}
        for k,v in hs.items():
            if v in hs2:
                return False
            else:
                hs2[v] = 1
        return True               
        
