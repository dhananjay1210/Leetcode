class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        def dfs(candidates,ind,target,combo_so_far):
            if target==0:
                final.append(combo_so_far)
                return
            if target < 0 or ind>=len(candidates):
                return 
            temp = combo_so_far[:]
            w1 = dfs(candidates,ind,target-candidates[ind],temp + [candidates[ind]])
            w2 = dfs(candidates,ind+1,target,temp)
        dfs(candidates,0,target,[])
        return final
