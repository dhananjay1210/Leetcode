class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        l = [[0]*4 for i in range(n+1)]
        
        for i in range(1,n+1):
            l[i][0],l[i][1],l[i][2],l[i][3] = l[i-1][0],l[i-1][1],l[i-1][2],l[i-1][3]
            ch = s[i-1]
            if ch == 'Q':
                l[i][0] += 1
            elif ch == 'W':
                l[i][1] += 1
            elif ch == 'E':
                l[i][2] += 1
            elif ch == 'R':
                l[i][3] += 1
        extra_q,extra_w,extra_r,extra_e = max(l[-1][0]-n//4,0),max(l[-1][1]-n//4,0),max(l[-1][2]-n//4,0),max(l[
            -1][3]-n//4,0)
        
        if extra_q==extra_w==extra_r==extra_e==0:
            return 0
        
        #print(l)
        mn = float("inf")
        for i in range(1,len(s)+1):
            start,end = i,n
            temp_start = i
            while temp_start < end:
                mid = (temp_start+end)//2
                #print("while : ",temp_start,mid,end)
                if (l[mid][0]-l[start-1][0] >= extra_q) and (l[mid][1]-l[start-1][1] >= extra_w) and (l[mid][2]
                    -l[start-1][2] >= extra_r) and (l[mid][3]-l[start-1][3] >= extra_e):
                    mn = min(mn,mid-start+1)
                    end = mid-1
                    #print(mn,end)
                else:
                    temp_start = mid+1 
            if (l[end][0]-l[start-1][0] >= extra_q) and (l[end][1]-l[start-1][1] >= extra_w) and (l[end][2]
                -l[start-1][2] >= extra_r) and (l[end][3]-l[start-1][3] >= extra_e):
                    mn = min(mn,end-start+1)
        return mn
