import unittest
from tictactoe2 import *


class TestAllFunctions(unittest.TestCase):
    def test_playerName(self):
        self.assertEqual(playerName(number='X', players={'X': '', 'O': ''}, name='John Doe'), {
                         'X': 'John Doe', 'O': ''}, "Should be {'X': 'John Doe', 'O': ''}")

    def test_checkWin(self):
        self.assertEqual(checkWin(board={'1': 'X', '2': 'X', '3': 'X',
                                         '4': 'O', '5': 'O', '6': '6',
                                         '7': '7', '8': '8', '9': '9'}, turn='X', condition=False),
                         True, "Should be True")


if __name__ == '__main__':
    unittest.main()
