class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        def dfs(candidates,ind,target,combo_so_far):
            if target==0:
                found = 0
                for f in final:
                    if sorted(f) == sorted(combo_so_far):
                        found = 1
                        break
                if found == 0:
                    final.append(combo_so_far)
                return
            if target < 0 or ind>=len(candidates):
                return 
            temp = combo_so_far.copy()
            w1 = dfs(candidates,ind+1,target-candidates[ind],temp + [candidates[ind]])
            w2 = dfs(candidates,ind+1,target,temp)
        dfs(candidates,0,target,[])
        return final
