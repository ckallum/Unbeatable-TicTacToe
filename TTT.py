
XPLAYER = +1
OPLAYER = -1
EMPTY = 0

board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def printBoard(brd):
    chars = {XPLAYER: 'X', OPLAYER: 'O', EMPTY: ' '}
    for x in brd:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n'+'---------------')


def clearBoard():
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = EMPTY


def gameOver(brd, player):
    winningStates = [[brd[0][0], brd[0][1], brd[0][2]],
                     [brd[1][0], brd[1][1], brd[1][2]],
                     [brd[2][0], brd[2][1], brd[2][2]],
                     [brd[0][0], brd[1][0], brd[2][0]],
                     [brd[0][1], brd[1][1], brd[2][1]],
                     [brd[0][2], brd[1][2], brd[2][2]],
                     [brd[0][0], brd[1][1], brd[2][2]],
                     [brd[0][2], brd[1][1], brd[2][0]]]

    if [player,player,player] in winningStates:
        return True

    return False


def emptyCells(brd):
    emptyC = []
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            if brd[x][y] == EMPTY:
                emptyC.append([x, y])

    return emptyC


def boardFull(brd):
    if len(emptyCells(brd)) == 0:
        return True
    return False


def playerMove(brd, player):
    e = True
    moves = {1:[0, 0], 2:[0,1], 3:[0,2],
             4:[1, 0], 5:[1, 1], 6:[1, 2],
             7:[2, 0], 8:[2, 1], 9:[2, 2]}
    while e:
        try:
            move = int(input('Pick a position(1-9)'))
            if move < 0 or move > 9:
                print('Invalid location! ')
            elif brd[moves[move][0]][moves[move][1]] != EMPTY:
                print('Location filled')
            else:
                brd[moves[move][0]][moves[move][1]] = player
                printBoard(brd)
                e = False
        except(KeyError, ValueError):
            print('Please pick a number!')


def switchPlayer(player):
    if player == XPLAYER:
        temp = OPLAYER
    else:
        temp = XPLAYER
    return temp


def main():
    while True:
        user = input('Play?(Y/N) ')
        if user.lower() == 'y':
            order = int(input('Would you like to go first(X) or second(O)? (1/2)? '))
        else:
            print('Bye!')
            exit()

        clearBoard()
        printBoard(board)

        if order == 1:
            player = XPLAYER
        else:
            player = OPLAYER

        while not(boardFull(board)):
            if gameOver(board, XPLAYER):
                print('X has won! ')
                break

            elif gameOver(board, OPLAYER):
                printBoard('O\'s have won! ')
                break

            else:
                playerMove(board, player)
                player = switchPlayer(player)
        else:
            print('Draw')


if __name__ == '__main__':
    main()
