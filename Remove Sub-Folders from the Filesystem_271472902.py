class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        from collections import Counter
        d = Counter(folder)
        l = []
        for i in folder:
            flag = 1
            for j in range(len(i)):
                if i[j]=="/" and i[:j] in d:
                    flag = 0
                    break
            if flag:
                l.append(i)
        return l
