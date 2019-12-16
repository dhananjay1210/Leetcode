class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        from collections import Counter
        d1 = Counter(s1)
        d2 = Counter(s2)
        ans = -1
        if (d1['x']+d2['x'])%2==(d1['y']+d2['y'])%2==0:
            x_y = 0
            y_x = 0
            ans = 0
            for i in range(len(s1)):
                if s1[i]=='x' and s2[i]=='y':
                    x_y += 1
                if s1[i]=='y' and s2[i]=='x':
                    y_x += 1
            ans += (x_y//2)
            ans += (y_x//2)
            if x_y%2==1:
                ans += 2
        return ans
