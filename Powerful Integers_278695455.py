class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1 and y==1:
            if bound<2:
                return []
            return [2]
        l1,l2 = [1],[1]
        while l1[-1] < 1000001 and x!=1:
            l1.append(l1[-1]*x)
        while l2[-1] < 1000001 and y!=1:
            l2.append(l2[-1]*y)
        ans = set()
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i]+l2[j] <= bound:
                    ans.add(l1[i]+l2[j])
                else:
                    break
        return list(ans)
