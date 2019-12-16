class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stc = []
        n = len(s)
        cnt = 0
        for i in range(n):
            if s[i]==')':
                if cnt>0:
                    stc.append(s[i])
                    cnt -= 1
            elif s[i]=='(':
                stc.append(s[i])
                cnt += 1
            else:
                stc.append(s[i])
        if cnt:
            temp = []
            while cnt:
                ele = stc.pop()
                if ele=='(':
                    cnt -= 1
                else:
                    temp.append(ele)
            while temp:
                stc.append(temp.pop())
        return "".join(stc)        
