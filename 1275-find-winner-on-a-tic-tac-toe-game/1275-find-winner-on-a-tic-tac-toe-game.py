class Solution:
    def tictactoe(self, moves):
        board = [[''] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'

        for player in ['X', 'O']:
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return 'A' if player == 'X' else 'B'

                if all(board[j][i] == player for j in range(3)):
                    return 'A' if player == 'X' else 'B'

            if all(board[i][i] == player for i in range(3)):
                return 'A' if player == 'X' else 'B'

            if all(board[i][2 - i] == player for i in range(3)):
                return 'A' if player == 'X' else 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'