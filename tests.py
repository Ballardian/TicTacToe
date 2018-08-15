import unittest
from unittest import mock
from unittest.mock import patch
import game_setup


class GameSetupTests(unittest.TestCase):
    board = game_setup.Game().board
    player_one_symbol = 'X'
    player_two_symbol = 'O'

    def test_board(self):
        self.assertIsNotNone(self.board, 'board is None')

    def test_build_board(self):
        result = game_setup.Game().build_board(self.board)
        self.assertIsNone(result)

    def test_check_input(self):
        choice = 'a'
        choice_2 = 1
        choice_3 = '-'
        choice_4 = 12
        result = game_setup.Game().check_input(choice)
        self.assertFalse(result)
        result_2 = game_setup.Game().check_input(choice_2)
        self.assertTrue(result_2)
        result_3 = game_setup.Game().check_input(choice_3)
        self.assertFalse(result_3)
        result_4 = game_setup.Game().check_input(choice_4)
        self.assertFalse(result_4)

    @mock.patch('builtins.input', side_effect=['1', '2'])
    def test_choose_symbol(self, mock_input):
        result_1 = game_setup.Game().choose_symbol()
        self.assertEqual(result_1, ('X', 'O'))
        result_2 = game_setup.Game().choose_symbol()
        self.assertEqual(result_2, ('O', 'X'))

    @mock.patch('builtins.input', return_value='1')
    def test_choose_turns(self, mock_input):
        game_type = 'pvp'
        result = game_setup.Game().choose_turns(game_type)
        self.assertEqual(result[0], 'player')
        self.assertNotEqual(result[1], 'computer')
        game_type_1 = 'cvc'
        result_1 = game_setup.Game().choose_turns(game_type_1)
        self.assertEqual(result_1[0], 'computer')
        self.assertEqual(result_1[1], 'computer')

    @mock.patch('builtins.input', side_effect=['1', '1', '2', '2'])
    def test_choose_turns_pvc(self, mock_inputs):
        game_type = 'pvc'
        result = game_setup.Game().choose_turns(game_type)
        self.assertEqual(result[0], 'player')
        self.assertEqual(result[1], 'computer')
        self.assertEqual(result[2], 'X')
        self.assertEqual(result[3], 'O')
        result_2 = game_setup.Game().choose_turns(game_type)
        self.assertEqual(result_2[0], 'computer')
        self.assertEqual(result_2[1], 'player')
        self.assertEqual(result_2[2], 'O')
        self.assertEqual(result_2[3], 'X')

    @patch('computer.AI.computer_move')
    def test_player_one_computer_move(self, mock):
        player_one = 'computer'
        game_setup.Game().player_one_move(player_one, self.player_one_symbol, self.player_two_symbol)
        self.assertTrue(mock.called)

    @patch('player.Player.human_move')
    def test_player_one_human_move(self, mock):
        player_one = 'player'
        game_setup.Game().player_one_move(player_one, self.player_one_symbol, self.player_two_symbol)
        self.assertTrue(mock.called)

    def test_game_is_over(self):
        player_symbol = 'X'
        # player_symbol = 'O'
        board = self.board
        board[0] = player_symbol
        board[1] = player_symbol
        board[2] = player_symbol
        result = game_setup.Game().game_is_over(board, player_symbol)
        board[3] = player_symbol
        board[4] = player_symbol
        board[5] = player_symbol
        result = game_setup.Game().game_is_over(board, player_symbol)
        board[6] = player_symbol
        board[7] = player_symbol
        board[8] = player_symbol
        result = game_setup.Game().game_is_over(board, player_symbol)
        self.assertTrue(result)

    def test_game_is_a_tie(self):
        player_one_symbol = self.player_one_symbol
        player_two_symbol = self.player_two_symbol
        board = self.board
        board[0] = player_one_symbol
        board[1] = player_one_symbol
        board[2] = player_two_symbol
        board[3] = player_two_symbol
        board[4] = player_one_symbol
        board[5] = player_two_symbol
        board[6] = player_two_symbol
        board[7] = player_two_symbol
        board[8] = player_one_symbol
        result = game_setup.Game().game_is_a_tie(board)
        self.assertTrue(result)

    @patch('game_setup.Game.game_is_a_tie')
    def test_check_state_of_game_game_is_tie(self, mock):
        result = game_setup.Game().check_state_of_game(self.board, self.player_one_symbol, self.player_two_symbol)
        self.assertTrue(mock.called)

    @patch('game_setup.Game.game_is_over')
    def test_check_state_of_game_player_wins(self, mock):
        result = game_setup.Game().check_state_of_game(self.board, self.player_one_symbol, self.player_two_symbol)
        self.assertTrue(mock.called)


if __name__ == '__main__':
    unittest.main()
