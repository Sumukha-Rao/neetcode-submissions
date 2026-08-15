class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        res=[]
        cols=set()
        posdiag=set()
        negdiag=set()
        def dfs(r):
            if r==n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]="Q"
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                dfs(r+1)
                board[r][c]="."
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        dfs(0)
        return res