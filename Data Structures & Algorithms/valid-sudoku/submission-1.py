class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=[[] for _ in board]
        boxes=[[] for _ in board] 
        rows=[[] for _ in board]
        n=len(board) 
        for r in range(n):
            for c in range(n):
                val=board[r][c]
                if val==".":
                    continue
                box=(r//3)*3+(c//3)
                if val in rows[r] or val in col[c] or val in boxes[box]:
                    return False
                rows[r].append(val)
                col[c].append(val)
                boxes[box].append(val)
        return True

                            


        
        
