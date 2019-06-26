def printBoard(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9]+'\n')


def clearBoard():
    board = [' ' for x in range(10)]
    return board


def getWinner(b, current):
    return (b[7] == current and b[8] == current and b[9] == current) or (b[4] == current and b[5] == current and b[6] == current) or(b[1] == current and b[2] == current and b[3] == current) or(b[1] == current and b[4] == current and b[7] == current) or(b[2] == current and b[5] == current and b[8] == current) or(b[3] == current and b[6] == current and b[9] == current) or(b[1] == current and b[5] == current and b[9] == current) or(b[3] == current and b[5] == current and b[7] == current)


def boardFull(b):
    return b.count(' ') == 1


def makeMove(b, player):
    e = True
    while e:
        try:
            move = int(input('Pick a position(1-9)'))
            if move < 0 or move > 9:
                print('Invalid location! ')
            elif b[move] != ' ':
                print('Location filled')
            else:
                b[move] = player
                printBoard(b)
                e = False
        except:
            print('Please pick a number!')



def switchPlayer(player):
    if player == 'X':
        temp = 'O'
    else:
        temp = 'X'
    return temp


def main(order):
    board = clearBoard()
    printBoard(board)
    if order == 1:
        player = 'X'
    else:
        player = 'O'

    while not(boardFull(board)):
        if getWinner(board, 'X'):
            print('X has won! ')
            break

        elif getWinner(board, 'O'):
            printBoard('O\'s have won! ')
            break

        else:
            makeMove(board, player)
            player = switchPlayer(player)
    else:
        print('Draw')


while True:
    user = input('Play?(Y/N) ')
    if user.lower() == 'y':
        order = int(input('Would you like to go first(X) or second(O)? (1/2)? '))
        main(int(order))
    else:
        break
