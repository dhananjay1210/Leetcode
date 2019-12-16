
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in "!?',;.":
            paragraph = paragraph.replace(i," ")
        para = paragraph.strip().lower().split()
        d1 = {}
        punc = {}
        for wrd in para:
            d1[wrd] = d1.get(wrd,0)+1
        mx_wrd,mx = '',0
        #print(d1)
        for i in d1.keys():
            if i not in banned and d1[i]>mx:
                mx = d1[i]
                mx_wrd = i
        return mx_wrd
                
            
