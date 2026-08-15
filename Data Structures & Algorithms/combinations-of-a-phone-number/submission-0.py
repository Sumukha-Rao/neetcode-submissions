class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res=[]
        def dfs(start,path):
            if start==len(digits):
                res.append("".join(path))
                return
            for i in phone[digits[start]]:
                path.append(i)
                dfs(start+1,path)
                path.pop()
        dfs(0,[])
        return res