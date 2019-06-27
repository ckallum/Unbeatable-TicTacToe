from random import choice
from math import inf

XPLAYER = +1
OPLAYER = -1
EMPTY = 0

board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]


def printBoard(brd):
    chars = {XPLAYER: 'X', OPLAYER: 'O', EMPTY: ' '}
    for x in brd:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n'+'---------------')


def clearBoard(brd):
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            brd[x][y] = EMPTY


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


def setMove(brd, x, y, player):
    brd[x][y] = player


def playerMove(brd):
    e = True
    moves = {1:[0, 0], 2:[0, 1], 3:[0, 2],
             4:[1, 0], 5:[1, 1], 6:[1, 2],
             7:[2, 0], 8:[2, 1], 9:[2, 2]}
    while e:
        try:
            move = int(input('Pick a position(1-9)'))
            if move < 1 or move > 9:
                print('Invalid location! ')
            elif not(moves[move] in emptyCells(brd)):
                print('Location filled')
            else:
                setMove(brd, moves[move][0],moves[move][1], XPLAYER)
                printBoard(brd)
                e = False
        except(KeyError, ValueError):
            print('Please pick a number!')


def evaluate(brd):
    score = 0
    score += evaluateLine(brd, 0, 0, 0, 1, 0, 2)
    score += evaluateLine(brd, 1, 0, 1, 1, 1, 2)
    score += evaluateLine(brd, 2, 0, 2, 1, 2, 2)
    score += evaluateLine(brd, 0, 0, 1, 0, 2, 0)
    score += evaluateLine(brd, 0, 1, 1, 1, 2, 1)
    score += evaluateLine(brd, 0, 2, 1, 2, 2, 2)
    score += evaluateLine(brd, 0, 0, 1, 1, 2, 2)
    score += evaluateLine(brd, 0, 2, 1, 1, 2, 0)
    return score


def evaluateLine(brd, x1, y1, x2, y2, x3, y3):
    score = 0
    if brd[x1][y1] == XPLAYER:
        score = 1
    elif brd[x1][y1] == OPLAYER:
        score = 1

    if brd[x2][y2] == XPLAYER:
        if score == 1:
            score = 10
        elif score == -1:
            return 0
        else:
            score = 1
    elif brd[x2][y2] == OPLAYER:
        if score == -1:
            score = 10
        elif score == 1:
            return 0
        else:
            score = -1

    if brd[x3][y3] == XPLAYER:
        if score > 0:
            score *= 10
        elif score < 0:
            return 0
        else:
            score = 1
    elif brd[x3][y3] == OPLAYER:
        if score < 0:
            score *= -10
        elif score > 0:
            return 0
        else:
            score = -1

    return score


def MiniMaxAB(brd, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or gameOver(brd, player):
        return [-1, -1, evaluate(brd)]

    else:
        for cell in emptyCells(brd):
            setMove(brd, cell[0], cell[1], player)
            score = MiniMaxAB(brd, depth - 1, alpha, beta, -player)[2]
            if player == XPLAYER:
                if score > alpha:
                    alpha = score
                    row = cell[0]
                    col = cell[1]

            elif score < beta:
                beta = score
                row = cell[0]
                col = cell[1]

            setMove(brd, cell[0], cell[1], EMPTY)

            if alpha >= beta:
                break

        if player == XPLAYER:
            return [row, col, alpha]

        else:
            return [row, col, beta]


def AIMove(brd):
    if len(emptyCells(brd)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        setMove(brd, x, y, OPLAYER)
        printBoard(brd)

    else:
        result = MiniMaxAB(brd, len(emptyCells(brd)), -inf, inf, OPLAYER)
        setMove(brd, result[0], result[1], OPLAYER)
        printBoard(brd)


def main():
    while True:
        user = input('Play?(Y/N) ')
        order = -1
        if user.lower() == 'y':
            while True:
                try:
                    order = int(input('Would you like to go first or second? (1/2)? '))
                    if not(order == 1 or order == 2):
                        print('Please pick 1 or 2')
                    else:
                        break
                except(KeyError, ValueError):
                    print('Enter a number')
        else:
            print('Bye!')
            exit()

        clearBoard(board)

        while not(boardFull(board) or gameOver(board, XPLAYER) or gameOver(board, OPLAYER)):
            if order == 2:
                AIMove(board)
                order = ''

            playerMove(board)
            AIMove(board)

        if gameOver(board, XPLAYER):
            print('X has won! ')

        elif gameOver(board, OPLAYER):
            print('O\'s have won! ')

        else:
            print('Draw')


if __name__ == '__main__':
    main()
