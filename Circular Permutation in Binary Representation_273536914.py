class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        n = (1<<n)
        mp = [0]*n
        res = 0
        for i in range(1,n):
            num = bin(i)[2:]
            str1 = [num[0]]
            for j in range(1,len(num)):
                str1.append(str(int(num[j])^int(num[j-1])))
            app = int("".join(str1),2)
            mp[i] = app
            if app==start:
                res = i
        return mp[res:] + mp[:res]
            
