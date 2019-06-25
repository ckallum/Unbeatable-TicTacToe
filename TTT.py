board = [' ' for x in range(10)]


def printBoard(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])


def main():
    printBoard(board)


while True:
    user = input('Welcome to TicTacToe, would you like to play(Y/N)?')
    if input == 'Y':
        main()
    else:
        print('Thanks for playing!')
        break
