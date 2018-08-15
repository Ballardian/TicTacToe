from game_setup import Game
import sys

def choose_game_type():
    print("Hello, please choose the type of game you wish to play.")
    while True:
        game_type = input("Please enter PvP for player vs player, PvC for player vs computer, "
                          "or CvC to watch the computer battle it out.\n").strip().lower()
        try:
            if game_type == 'pvp' or game_type == 'pvc' or game_type == 'cvc':
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Try again.')
    print("You chose the {} game type.".format(game_type))
    if game_type == 'pvc':
        game = Game()
        game.run(game_type)
    elif game_type == 'pvp':
        game = Game()
        game.run(game_type)
    else:
        game = Game()
        game.run(game_type)

def play_again():
    while True:
        play_game_again = input("Play again (yes/no)\n").strip().lower()
        try:
            if play_game_again == 'yes':
                choose_game_type()
            elif play_game_again == 'no':
                print('Goodbye, see you next time.')
                sys.exit(0)
            else:
                raise ValueError
        except ValueError:
            print('Please enter yes or no.\n')


choose_game_type()
play_again()
