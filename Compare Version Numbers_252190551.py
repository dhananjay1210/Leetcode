class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = v1.split()
        v2 = v2.split()
        if v1[0]=='.':
            v1[0]='0.'
        if v1[-1]=='.':
            v1[-1]='.0'
        if v2[0]=='.':
            v2[0]='0.'
        if v2[-1]=='.':
            v2[-1]='.0'
        v1 = ''.join(v1)
        v2 = ''.join(v2)
        arr1 = v1.split(".") 
        arr2 = v2.split(".") 
        l1 = len(arr1)
        l2 = len(arr2)
        if l1<l2:
            for i in range(l2-l1):
                arr1.append('0')
        elif l2<l1:
            for i in range(l1-l2):
                arr2.append('0')

        i = 0 
        while(i < len(arr1)):

            if int(arr2[i]) > int(arr1[i]): 
                return -1
            if int(arr1[i]) > int(arr2[i]): 
                return 1

            i += 1

        return 0
        
