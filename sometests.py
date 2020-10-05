import unittest
from unittest.mock import patch
from tictactoe2 import *


class TestAllFunctions(unittest.TestCase):
    # upon prompt, key in John Doe for this to pass
    @patch('tictactoe2.checkalpha')
    def test_checkalpha(self, input):
        self.assertEqual(checkalpha("1"), 'John Doe', 'You entered John Doe')

    def test_playerName(self):
        self.assertEqual(playerName(number='X', players={'X': '', 'O': ''}, name='John Doe'), {
                         'X': 'John Doe', 'O': ''}, "Should be {'X': 'John Doe', 'O': ''}")

    def test_checkWin(self):
        self.assertEqual(checkWin(board={'1': 'X', '2': 'X', '3': 'X',
                                         '4': 'O', '5': 'O', '6': '6',
                                         '7': '7', '8': '8', '9': '9'}, turn='X', condition=False),
                         True, "Should be True")

    @patch('tictactoe2.checkBox')
    def test_checkBox(self, input):
        # only input 3 would pass the test
        self.assertEqual(checkBox(board={'1': 'X', '2': 'O', '3': '3',
                                         '4': '4', '5': '5', '6': '6',
                                         '7': '7', '8': '8', '9': '9'},
                                  players={'X': 'John Doe', 'O': 'Michael Doe'}, turn='X'),
                         {'1': 'X', '2': 'O', '3': 'X',
                          '4': '4', '5': '5', '6': '6',
                          '7': '7', '8': '8', '9': '9'})


if __name__ == '__main__':
    unittest.main()
