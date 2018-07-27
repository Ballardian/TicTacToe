import game


class PvP(game.Game):
    player_one = None
    player_two = None

    def choosing_symbols(self):
        # Choosing a symbol for player one
        while True:
            player_move_symbol = input("Please choose a symbol for player one i.e. 'X' or 'O'.\n").strip().upper()
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
        # Loop through until the game was won or tied
        # Player one's turn
        while not self.check_state_of_game(self.board, self.player_one, self.player_two):
            print("Player one's turn...")
            self.human_player_move(self.board, self.player_one)
            self.build_board()
            # Player two's turn
            if not self.check_state_of_game(self.board, self.player_one, self.player_two):
                print("Player two's turn...")
                self.human_player_move(self.board, self.player_two)
            self.build_board()