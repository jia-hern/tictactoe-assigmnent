def checkalpha():  # 1 this functions checks that string contains at least 1 letter
    while True:
        string = input('Type in a string: ')
        if (any(c.isalpha() for c in string)):
            return string
        else:
            print('Please enter a string with at least an alphabet')


def playerName(number, players, name):  # 2 this function adds a new player name to a dictionary
    players[number] = name


def checkBox(board, turn):  # 3 this functions checks if board location is occupied/ a number
    while True:
        move = input('Choose an unoccupied place on the board: ')
        if move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('key in a number from 1-9!')
        elif board[move] in ('X', 'O'):
            print('That place is already filled.\nMove to which place?')
        elif board[move] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            board[move] = turn
            return board


def checkWin(board, turn, condition):  # 5 this function checks for 3 connecting points
    if board['7'] == board['8'] == board['9']:  # across the bottom
        condition = True
        return condition
    elif board['4'] == board['5'] == board['6']:  # across the middle
        condition = True
        return condition
    elif board['1'] == board['2'] == board['3']:  # across the top
        condition = True
        return condition
    elif board['1'] == board['4'] == board['7']:  # down the left side
        condition = True
        return condition
    elif board['2'] == board['5'] == board['8']:  # down the middle
        condition = True
        return condition
    elif board['3'] == board['6'] == board['9']:  # down the right side
        condition = True
        return condition
    elif board['7'] == board['5'] == board['3']:  # diagonal
        condition = True
        return condition
    elif board['1'] == board['5'] == board['9']:  # diagonal
        condition = True
        return condition


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
