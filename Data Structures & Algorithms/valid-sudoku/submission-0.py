class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = {}
        c = {}
        s = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in r.get(i, set()):
                    return False
                if board[i][j] in c.get(j, set()):
                    return False
                if board[i][j] in s.get((i//3) * 3 + j//3, set()):
                    return False

                
                r.setdefault(i, set()).add(board[i][j])
                c.setdefault(j, set()).add(board[i][j])
                s.setdefault((i//3) * 3 + j//3, set()).add(board[i][j])
        return True




         