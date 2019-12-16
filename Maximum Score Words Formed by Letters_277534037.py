class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        d = Counter(letters)
        n = len(words)
        
        def rec(ind,d):
            if ind>=n:
                return 0
            
            way1,way2 = 0,0
            sc,new_d,poss = 0,d.copy(),1
            for ch in words[ind]:
                if ch in new_d and new_d[ch]>0:
                    sc += score[ord(ch)-97]
                    new_d[ch] -= 1
                else:
                    poss = 0
            if poss:
                way1 = sc + rec(ind+1,new_d)
            way2 = rec(ind+1,d)
            return max(way1,way2)
        return rec(0,d)
