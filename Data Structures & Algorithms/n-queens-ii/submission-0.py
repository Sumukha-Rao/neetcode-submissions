class Solution:
    def totalNQueens(self, n: int) -> int:
        cols,posdiag,negdiag=set(),set(),set()
        solutions=0
        def backtrack(row):
            if row==n:
                nonlocal solutions
                solutions+=1
                return 
            for col in range(n):
                if col in cols or (row+col) in posdiag or (row-col) in negdiag:
                    continue
                cols.add(col)
                posdiag.add(row+col)
                negdiag.add(row-col)
                backtrack(row+1)
                posdiag.remove(row+col)
                negdiag.remove(row-col)
                cols.remove(col)
        backtrack(0)
        return solutions



        