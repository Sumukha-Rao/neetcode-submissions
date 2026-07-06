class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=[]
        while columnNumber>0:
            columnNumber-=1
            col=columnNumber%26
            ans.append(chr(ord("A")+col))
            columnNumber//=26
        return "".join(reversed(ans))
       
