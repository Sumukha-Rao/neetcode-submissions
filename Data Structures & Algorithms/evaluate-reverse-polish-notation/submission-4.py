class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                op=tokens[i]
                res=None
                if op=="+":
                    res=a+b
                elif op=="-":
                    res=a-b
                elif op=="/":
                    res=int(a/b)
                else :
                    res=a*b
                stack.append(res)
        return stack[0]
