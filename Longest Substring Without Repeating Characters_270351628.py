class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        d = Counter()
        cnt = i = 0
        for j in range(len(s)):
            d[s[j]] += 1
            while d[s[j]]>1:
                d[s[i]] -= 1
                i += 1
            if j-i+1 > cnt:
                cnt = j-i+1
        return cnt
