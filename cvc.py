import game
import time

class CvC(game.Game):
    player_one = None
    player_two = None

    def choosing_symbols(self):
        # Choose symbols for computer players
        while True:
            player_move_symbol = input("Please choose a symbol "
                                       "for computer player one i.e. 'X' or 'O'.\n").strip().upper()
            try:
                if player_move_symbol == 'X' or player_move_symbol == 'O':
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again.")
        print("You chose the '{}' symbol for player one.".format(player_move_symbol))
        if player_move_symbol == 'X':
            self.player_one = 'X'
            self.player_two = 'O'
        else:
            self.player_one = 'O'
            self.player_two = 'X'
        return self.player_one, self.player_two

    def start_game(self, choosing_symbols):
        # loop through until the game was won or tied
        # Computer 1's turn
        while not self.check_state_of_game(self.board, self.player_one, self.player_two):
            move = self.computer_move(self.board, self.player_one, self.player_two)
            time.sleep(2)
            self.board[move] = self.player_one
            print('Computer one chose {}...'.format(move+1))
            self.build_board()
            # Computer 2's turn
            if not self.check_state_of_game(self.board, self.player_one, self.player_two):
                    move = self.computer_move(self.board, self.player_two, self.player_one)
                    time.sleep(2)
                    self.board[move] = self.player_two
                    print('Computer two chose {}...'.format(move+1))
            self.build_board()