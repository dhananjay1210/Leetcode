class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        from itertools import permutations
        if A[0]==A[1]==A[2]==A[3]==0:
            return "00:00"
        
        p = permutations(A)
        ans = "00:00"
        
        def compare(ans,i):
            ans_hr,ans_min = list(map(int,ans.split(":")))
            i_hr,i_min = int(str(i[0])+str(i[1])),int(str(i[2])+str(i[3]))
            
            if (i_hr>ans_hr and i_hr<24 and i_min < 60) or (i_hr==ans_hr and i_hr<24 and i_min>ans_min and i_min < 
                60):
                return str(i_hr)+":"+str(i_min)
            return ans
            #print(ans_hr,ans_min,i_hr,i_min)
        for i in p:
            #print(i)
            ans = compare(ans,i)
        if ans!="00:00":
            ans_hr,ans_min = ans.split(":")
            if len(ans_hr)<2:
                ans_hr = "0"+ans_hr
            if len(ans_min)<2:
                ans_min = "0"+ans_min
            return ans_hr+":"+ans_min
        else:
            return ""
