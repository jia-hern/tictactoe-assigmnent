# 2 Player Tic-Tac-Toe game in Python

''' use a dictonary as the board '''

theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' This function print the board everytime by calling this function when called
    This allows board to be updated on every turn '''


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# This function has all the gameplay functionality.
def game():
    # first player places x
    turn = 'X'
    players = {'X': '', 'O': ''}
    count = 0
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # ask players for their names:
    players['X'] = input('Enter name for Player 1: ')
    players['O'] = input('Enter name for Player 2: ')

    for _ in range(10):
        printBoard(theBoard)
        print(players[turn] + ", choose a box to place an " + turn + " into:")

        move = input()

        if theBoard[move] in numbers:
            # if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Check if player 1 or 2 has won (minimally need 5 turns)
        # 8 possible scenarios
        def printFinish(turn):
            print("Congratulations " +
                  players[turn] + "! You have won.")

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] in ['X', '0']:  # across the bottom
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] in ['X', '0']:  # across the middle
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] in ['X', '0']:  # across the top
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] in ['X', '0']:  # down the left side
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] in ['X', '0']:  # down the middle
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] in ['X', '0']:  # down the right side
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] in ['X', '0']:  # diagonal
                printBoard(theBoard)
                printFinish(turn)
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] in ['X', '0']:  # diagonal
                printBoard(theBoard)
                printFinish(turn)
                break

        # If neither player 1 nor 2 wins and the board is full, declare 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Toggle turn upon ever move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Ask if players want to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = key

        game()


if __name__ == "__main__":
    game()

# include prompt for player names
# need to change statement to player, "choose a box to place an", .. "into:"
