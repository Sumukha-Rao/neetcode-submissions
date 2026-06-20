class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opensymbol=["[","{","("]
        closesymbol=["]","}",")"]
        for symbol in s:
            if symbol in opensymbol:
                stack.append(symbol)
            elif stack and opensymbol.index(stack[-1]) == closesymbol.index(symbol) :
                stack.pop()
            else :
                return False
        if stack==[] :
            return True
        else:
            return False

        