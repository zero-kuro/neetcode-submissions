class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        col = []
        square = []
        a = 0
        b = 0
        c = 1
        d = 1
        

        import numpy as np
        sudoku = np.array(board)

        for i in range(sudoku.shape[0]): #checkbyrow
            while a < 9:
                if sudoku[i,a] != ".":
                    row.append(sudoku[i,a])
                a += 1
            if len(row) != len(set(row)):
                return False
            row = []
            a = 0

        for j in range(sudoku.shape[1]): #checkbycol
            while b < 9:
                if sudoku[b,j] != ".":
                    col.append(sudoku[b,j])
                b += 1
            if len(col) != len(set(col)):
                return False
            col = []
            b = 0
        

        while c < 8:
            while d < 8:
                for h in range(-1,2):
                    for k in range(-1,2):
                        if sudoku[c+h, d+k] != ".":
                            square.append(sudoku[c+h, d+k])
                if len(square) != len(set(square)):
                    return False
                square = []        
                d += 3
            d = 1
            c += 3
        
        return True

                


        





        