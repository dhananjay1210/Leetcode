class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {}
        res = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            if 'L' in d and 'R' in d and d['L'] == d['R']:
                res += 1
                d = {}
        return res
