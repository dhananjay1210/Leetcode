class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        flag = 1
        while flag:
            prev = arr[:]
            flag = 0
            for i in range(len(prev)-2,0,-1):
                if prev[i-1]>prev[i]<prev[i+1]:
                    arr[i] +=1
                    flag = 1
                elif prev[i-1]<prev[i]>prev[i+1]:
                    arr[i] -=1
                    flag = 1
        return arr        
