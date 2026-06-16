class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRepeat(chunk:List[str])->bool:
            chunk=[x for x in chunk if x!="."]
            return len(set(chunk))==len(chunk)
        col=[[] for _ in board]
        boxes=[[] for _ in board] 
        n=len(board) 
        for r in range(n):
            if checkRepeat(board[r])==False:
                return False
            for c in range(n):
                col[c].append(board[r][c])
                box=(r//3)*3+(c//3)
                boxes[box].append(board[r][c])
        for i in range(n):
            if checkRepeat(col[i])==False:
                return False
            if checkRepeat(boxes[i])==False:
                return False
        return True

                            


        
        
