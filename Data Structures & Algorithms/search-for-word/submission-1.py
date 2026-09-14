class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        import numpy as np
        board = np.array(board)
        rows, cols = board.shape
         
        pin = np.argwhere(board == word[0])
            
        def search(y,x, index, visited):
            directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]
            if len(visited) == len(word):
                    return True

            for dy, dx in directions:
                newy = y + dy
                newx = x + dx
                if newy < 0 or newy >= rows:
                    continue
                if newx < 0 or newx >= cols:
                    continue
                if board[newy,newx] == word[index] and [newy,newx] not in visited:
                    if search(newy, newx, index+1, visited + [[newy,newx]]) == True:
                        return True
        
        for p in pin:
            y,x = p
            visited = [[y,x]]
            if search(y, x, 1, visited) == True:
                return True
        return False
        
        
                

                
