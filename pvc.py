import game


class PvC(game.Game):
    def choosing_symbols(self):
        # Choosing which player goes first
        while True:
            player_one = input("Please choose which player goes first. "
                                  "Please enter 'player' or 'computer'.\n")
            player_one = player_one.strip().lower()
            try:
                if str(player_one) == 'player' or str(player_one) == 'computer':
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again.")
        print("You chose the {} to go first.".format(player_one))
        # Choosing the symbol for player one
        while True:
            player_move_symbol = input("Please choose a symbol for player one i.e. 'X' or 'O'.\n").strip().upper()
            try:
                if player_move_symbol == 'X' or player_move_symbol == 'O':
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again.")
        print("You chose '{}' for player one.".format(player_move_symbol))
        if player_one == 'player' and player_move_symbol == 'X' or \
                player_one == 'computer' and player_move_symbol == 'O':
            self.human_player = 'X'
            self.computer_player = 'O'
        else:
            self.human_player = 'O'
            self.computer_player = 'X'
        return player_one

    def start_game(self, player_one):
        # Loop through until the game was won or tied
        # player one's turn
        while not self.check_state_of_game(self.board, self.computer_player, self.human_player):
            if player_one == 'player':
                self.human_player_move(self.board, self.human_player)
            elif player_one == 'computer':
                move = self.computer_move(self.board, self.computer_player, self.human_player)
                self.board[move] = self.computer_player
                print('Computer chose {}...'.format(move+1))
            self.build_board()
            # player two's turn
            if not self.check_state_of_game(self.board, self.computer_player, self.human_player):
                if player_one == 'player':
                    move = self.computer_move(self.board, self.computer_player, self.human_player)
                    self.board[move] = self.computer_player
                    print('Computer chose {}...'.format(move+1))
                elif player_one == 'computer':
                    self.human_player_move(self.board, self.human_player)
            self.build_board()

    def check_state_of_game(self, board, player_one, player_two):
        # Check if the game has been won or tied
        if self.game_is_a_tie(board):
            print('The game is a tie.')
            return True
        elif self.game_is_over(board, self.computer_player):
            print('Computer wins.')
            return True
        elif self.game_is_over(board, self.human_player):
            print('Player wins.')
            return True
        else:
            return False