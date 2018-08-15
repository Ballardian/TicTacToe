class Player:

    def human_move(self, board, human_player_symbol):
        # Human player move = move_choice -1 to make player input match board index
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
        print('Player chose {}...'.format(move_choice+1))