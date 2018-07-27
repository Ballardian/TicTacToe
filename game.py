import time


class Game:

    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.computer_player = "X"
        self.human_player = "O"


    def build_board(self):
        # Build the board
        print(" %s  %s  %s \n %s  %s  %s \n %s  %s  %s \n" % \
              (self.board[0], self.board[1], self.board[2],
               self.board[3], self.board[4], self.board[5],
               self.board[6], self.board[7], self.board[8]))

    def game_is_over(self, board, player_symbol):
        # Check if game has been won
        return ((board[0] == player_symbol and board[1] == player_symbol and board[2] == player_symbol) or
                (board[3] == player_symbol and board[4] == player_symbol and board[5] == player_symbol) or
                (board[6] == player_symbol and board[7] == player_symbol and board[8] == player_symbol) or
                (board[0] == player_symbol and board[3] == player_symbol and board[6] == player_symbol) or
                (board[1] == player_symbol and board[4] == player_symbol and board[7] == player_symbol) or
                (board[2] == player_symbol and board[5] == player_symbol and board[8] == player_symbol) or
                (board[0] == player_symbol and board[4] == player_symbol and board[8] == player_symbol) or
                (board[2] == player_symbol and board[4] == player_symbol and board[6] == player_symbol))

    def game_is_a_tie(self, b):
        # Check if game is a tie
        return len([s for s in b if s == "X" or s == "O"]) == 9


    def test_winning_move(self, board, player_symbol, test_move):
        # Test if any available moves could win the game
        copy_of_board = self.create_copy_of_board(self.board)
        copy_of_board[test_move] = player_symbol
        return self.game_is_over(copy_of_board, player_symbol)

    def computer_move(self, board, computer, opponent):
        # Delay computer move by 1 sec
        time.sleep(1)
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
        # Make a duplicate of the board to test winning moves on
        duplicate_board = []
        for j in board:
            duplicate_board.append(j)
        return duplicate_board

    def human_player_move(self, board, human_player_symbol):
        # Human player move - move_choice -1 to make player input match board index
        while True:
            move_choice = input('Please choose a number corresponding to a square -'
                                ' choose a number between 1 and 9...\n')
            try:
                if int(move_choice) in range(1, 10) and board[(int(move_choice)-1)] != 'X' \
                        and board[(int(move_choice)-1)] != 'O':
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number, referring to an unoccupied square on the board.")
        move_choice = (int(move_choice)-1)
        board[move_choice] = human_player_symbol
        print('Player chose {}...'.format(move_choice))

    def check_state_of_game(self, board, player_one, player_two):
        # Check if the game has been won or tied
        if self.game_is_a_tie(board):
            print('The game is a tie.')
            return True
        elif self.game_is_over(board, player_one):
            print('Player one wins.')
            return True
        elif self.game_is_over(board, player_two):
            print('Player two wins.')
            return True
        else:
            return False

    def run(self):
        self.build_board()
        self.start_game((self.choosing_symbols()))