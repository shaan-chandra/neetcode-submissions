class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # ok this seems easy
        # just run dfs from internal o's til before rows - 1 and cols - 1
        rows, cols = len(board), len(board[0])
        # just dont run dfs on edge of board 
        def dfs(r,c):
            #print("row: ", r, "col: ", c)
            if r not in range(rows) or c not in range(cols) or board[r][c] != 'O':
                return
            board[r][c] = 'S'
            #print("board here: ", board)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # key is all surronded cells are safe so 
        # run dfs from surronded cells mark them safe
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        #print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        #print(board)