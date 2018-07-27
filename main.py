import cvc
import pvp
import pvc
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
        game = pvc.PvC()
        game.run()
    elif game_type == 'pvp':
        game = pvp.PvP()
        game.run()
    else:
        game = cvc.CvC()
        game.run()

def play_again():
    while True:
        play_again = input("Play again (yes/no)\n").strip().lower()
        try:
            if play_again == 'yes':
                choose_game_type()
            elif play_again == 'no':
                sys.exit(0)
            else:
                raise ValueError
        except ValueError:
            print('Please enter yes or no.\n')


choose_game_type()
play_again()