from player import Player
from computer import AI

class Game:

    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def build_board(self, board):
        # Build the board
        print(" %s  %s  %s \n %s  %s  %s \n %s  %s  %s \n" % \
              (board[0], board[1], board[2],
               board[3], board[4], board[5],
               board[6], board[7], board[8]))

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

    def game_is_a_tie(self, board):
        # Check if game is a tie
        return len([square for square in board if square == "X" or square == "O"]) == 9

    def check_state_of_game(self, board, player_one_symbol, player_two_symbol):
        # Check if the game has been won or tied
        if self.game_is_a_tie(board):
            print('The game is a tie.')
            return True
        elif self.game_is_over(board, player_one_symbol):
            print('Player one wins.')
            return True
        elif self.game_is_over(board, player_two_symbol):
            print('Player two wins.')
            return True
        else:
            return False

    def choose_symbol(self):
        while True:
            player_one_symbol = input('Choose the symbol for player one:\n'
                                      '1. X \n'
                                      '2. O \n').strip()
            if self.check_input(player_one_symbol):
                print('You have chosen option {}.'.format(player_one_symbol))
                break
            else:
                print("Invalid choice. Try again.")
        if player_one_symbol == '1':
            player_one_symbol = 'X'
            player_two_symbol = 'O'
            return player_one_symbol, player_two_symbol
        else:
            player_one_symbol = 'O'
            player_two_symbol = 'X'
            return player_one_symbol, player_two_symbol

    def check_input(self, choice):
        try:
            if 0 < int(choice) <= 2:
                return True
        except ValueError:
            print("Invalid choice. Try again.")
            return False

    def choose_turns(self, game_type):
        if game_type == 'pvp':
            player_one, player_two = 'player', 'player'
            symbols = self.choose_symbol()
            player_one_symbol, player_two_symbol = symbols[0], symbols[1]
            return player_one, player_two, player_one_symbol, player_two_symbol
        elif game_type == 'pvc':
            while True:
                choice = input('Choose player one:\n'
                               '1. Player \n'
                               '2. Computer \n').strip()
                if self.check_input(choice):
                    print('You have chosen option {}.'.format(choice))
                    break
            if choice == '1':
                player_one, player_two = 'player', 'computer'
                symbols = self.choose_symbol()
                player_one_symbol, player_two_symbol = symbols[0], symbols[1]
                return player_one, player_two, player_one_symbol, player_two_symbol
            else:
                player_one, player_two = 'computer', 'player'
                symbols = self.choose_symbol()
                player_one_symbol, player_two_symbol = symbols[0], symbols[1]
                return player_one, player_two, player_one_symbol, player_two_symbol
        elif game_type == 'cvc':
            player_one, player_two = 'computer', 'computer'
            symbols = self.choose_symbol()
            player_one_symbol, player_two_symbol = symbols[0], symbols[1]
            return player_one, player_two, player_one_symbol, player_two_symbol

    def player_one_move(self, player_one, player_one_symbol, player_two_symbol):
        if player_one == 'player':
            return Player().human_move(self.board, player_one_symbol)
        elif player_one == 'computer':
            move = AI().computer_move(self.board, player_one_symbol, player_two_symbol)
            self.board[move] = player_one_symbol

    def player_two_move(self, player_two, player_two_symbol, player_one_symbol):
        if player_two == 'player':
            return Player().human_move(self.board, player_two_symbol)
        elif player_two == 'computer':
            move = AI().computer_move(self.board, player_two_symbol, player_one_symbol)
            self.board[move] = player_two_symbol

    def start_game(self, player_one, player_two, player_one_symbol, player_two_symbol):
        # Loop through until the game was won or tied
        # Player one's turn
        while not self.check_state_of_game(self.board, player_one_symbol, player_two_symbol):
            print("Player one's turn...")
            self.player_one_move(player_one, player_one_symbol, player_two_symbol)
            self.build_board(self.board)
            # Player two's turn
            if not self.check_state_of_game(self.board, player_one_symbol, player_two_symbol):
                print("Player two's turn...")
                self.player_two_move(player_two, player_two_symbol, player_one_symbol)
            self.build_board(self.board)

    def run(self, game_type):
        Game().build_board(Game().board)
        Game().start_game(*Game().choose_turns(game_type))