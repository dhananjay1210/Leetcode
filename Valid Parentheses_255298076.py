class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        for i in s:
            if i in ['(','[','{']:
                stc.append(i)
            elif stc and ((i==')'and stc[-1]=='(') or (i==']'and stc[-1]=='[') or (i=='}'and stc[-1]=='{')):
                stc.pop()
            else:
                return False
        if stc:
            return False
        return True
        
