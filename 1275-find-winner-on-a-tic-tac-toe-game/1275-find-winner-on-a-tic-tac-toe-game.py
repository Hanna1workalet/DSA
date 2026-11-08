class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        row = [0]*3
        col = [0]*3
        diag1 = 0
        diag2 = 0
        xo = 1
        for r,c in moves:
            row[r] += xo
            col[c] += xo
            if r == c:
                diag1 += xo
            if r + c == 2:
                diag2 += xo
            if abs(row[r]) == 3 or abs(col[c]) == 3 or abs(diag1) == 3 or abs(diag2) == 3:
                if xo == 1:
                    return "A"
                elif xo == -1:
                    return "B"
            xo*=-1
        if len(moves) < 9:
            return "Pending"    
        else:
            return "Draw"