from tictactoe2 import *

board = {'1': '1', '2': '2', '3': '3',
         '4': '4', '5': '5', '6': '6',
         '7': '7', '8': '8', '9': '9'}
board_keys = []

# to get a list of the keys
for key in board:
    board_keys.append(key)


def game():
    turn = 'X'
    count = 0
    condition = False
    players = {'X': '', 'O': ''}

    # ask players for names
    name1 = checkalpha("1")
    name2 = checkalpha("2")

    playerName(number='X', players=players, name=name1)
    playerName(number='O', players=players, name=name2)

    for _ in range(9):
        # ask for user input for placement on board
        currentBoard = checkBox(board, players, turn)
        # show the tictactoe board
        printBoard(currentBoard)
        count += 1
        # can skip checking for wins in the first 4 turns:
        if count >= 5:
            condition = checkWin(currentBoard, turn, condition)
        # exit loop if win condition detected
        if(condition):
            print("Congratulations " + players[turn] + "! You have won :D")
            break

        # end game if tie
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
        # Toggle turn upon ever move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # ask if players want to restart the game
    restart = input('Do you want to play again? (y/n) ')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            board[key] = key
        game()


if __name__ == "__main__":
    game()
