import game_setup
import time


class AI:

    def test_winning_move(self, board, player_symbol, test_move):
        # Test if any available moves could win the game
        copy_of_board = self.create_copy_of_board(board)
        copy_of_board[test_move] = player_symbol
        return game_setup.Game().game_is_over(copy_of_board, player_symbol)

    def computer_move(self, board, computer, opponent):
        # Delay computer move by 1 sec
        time.sleep(2)
        # Check for computer win move
        for move in range(0, 9):
            if board[move] != 'X' and board[move] != 'O' and self.test_winning_move(board, computer, move):
                return move
        # Check opponent win moves
        for move in range(0, 9):
            if board[move] != 'X' and board[move] != 'O' and self.test_winning_move(board, opponent, move):
                return move
        # Play center
        if board[4] != 'X' and board[4] != 'O':
            return 4
        # Play a corner
        for move in [0, 2, 6, 8]:
            if board[move] != 'X' and board[move] != 'O':
                return move
        # Play a side
        for move in [1, 3, 5, 7]:
            if board[4] != 'X' and board[4] != 'O':
                return move
        # Play any if non available
        for move in range(0, 9):
            if board[move] != 'X' and board[move] != 'O':
                return move

    def create_copy_of_board(self, board):
        # Make a duplicate of the current board to test winning moves on
        duplicate_board = []
        for square in board:
            duplicate_board.append(square)
        return duplicate_board
