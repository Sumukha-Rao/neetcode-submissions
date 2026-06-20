class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}
        count2={}
        for i in range(97,123):
            count1[chr(i)]=0
            count2[chr(i)]=0
        n=len(s1)
        for i in s1:
            count1[i]=count1.get(i,0)+1
        left=0
        
        window=0
        for right in range(len(s2)):
            count2[s2[right]]=count2.get(s2[right],0)+1
            window+=1
            if window>n:
                count2[s2[left]]-=1
                left+=1
            if count1==count2:
                return True    
        return False
            
        

        