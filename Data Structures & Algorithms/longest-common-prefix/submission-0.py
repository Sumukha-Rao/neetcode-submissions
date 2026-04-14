class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfix=strs[0]
        i=0
        while i<len(strs)-1:
            if pfix in strs[i] and pfix in strs[i+1]:
                i+=1
            else:
                pfix=pfix[:-1]            
        return pfix


        