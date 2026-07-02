class Solution(object):

    # Down, Up, Right, Left
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    def valid(self, i, j, m, n):

        if i < 0 or i >= n or j < 0 or j >= m:
            return False

        return True

    def dfs(self, board, m, n, i, j):

        # Mark current cell as safe
        board[i][j] = '#'

        # Visit all 4 directions
        for k in range(4):

            row = i + self.x[k]
            col = j + self.y[k]

            if (self.valid(row, col, m, n) and
                board[row][col] == 'O'):

                self.dfs(board, m, n, row, col)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        n = len(board)
        m = len(board[0])

        # Left Boundary
        for i in range(n):

            if board[i][0] == 'O':
                self.dfs(board, m, n, i, 0)

        # Right Boundary
        for i in range(n):

            if board[i][m - 1] == 'O':
                self.dfs(board, m, n, i, m - 1)

        # Top Boundary
        for j in range(m):

            if board[0][j] == 'O':
                self.dfs(board, m, n, 0, j)

        # Bottom Boundary
        for j in range(m):

            if board[n - 1][j] == 'O':
                self.dfs(board, m, n, n - 1, j)

        # Convert the board
        for i in range(n):
            for j in range(m):

                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == '#':
                    board[i][j] = 'O'