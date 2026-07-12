class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=[set() for _ in board]
        boxes=[set() for _ in board] 
        rows=[set() for _ in board]
        n=len(board) 
        for r in range(n):
            for c in range(n):
                val=board[r][c]
                if val==".":
                    continue
                box=(r//3)*3+(c//3)
                if val in rows[r] or val in col[c] or val in boxes[box]:
                    return False
                rows[r].add(val)
                col[c].add(val)
                boxes[box].add(val)
        return True

                            


        
        
