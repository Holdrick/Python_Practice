import pprint
import random

tttBoard = {'topL':' ', 'topM':' ', 'topR':' ',
            'midL':' ', 'midM':' ', 'midR':' ',
            'botL':' ', 'botM':' ', 'botR':' '}

tttMoves = ['topL', 'topM', 'topR',
            'midL', 'midM', 'midR',
            'botL', 'botM', 'botR']

validShapes = ['X', 'x', 'O', 'o']

player = ''
AI = ''


def winner():
    if tttBoard['topL'] in validShapes:
        if tttBoard['topL'] == tttBoard['topM'] == tttBoard['topR']:
            return True
        elif tttBoard['topL'] == tttBoard['midM'] == tttBoard['botR']:
            return True
        elif tttBoard['topL'] == tttBoard['midL'] == tttBoard['botL']:
            return True

    if tttBoard['topM'] in validShapes:
        if tttBoard['topM'] == tttBoard['midM'] == tttBoard['botM']:
            return True

    if tttBoard['topR'] in validShapes:
        if tttBoard['topR'] == tttBoard['midR'] == tttBoard['botR']:
            return True
        elif tttBoard['topR'] == tttBoard['midM'] == tttBoard['botL']:
            return True

    if tttBoard['midL'] in validShapes:
        if tttBoard['midL'] == tttBoard['midM'] == tttBoard['midR']:
            return True

    if tttBoard['botL'] in validShapes:
        if tttBoard['botL'] == tttBoard['botM'] == tttBoard['botR']:
            return True    

    return False


def printBoard():
    print('')
    print(tttBoard['topL'] + '|' + tttBoard['topM'] + '|' + tttBoard['topR'])
    print('------')
    print(tttBoard['midL'] + '|' + tttBoard['midM'] + '|' + tttBoard['midR'])
    print('------')
    print(tttBoard['botL'] + '|' + tttBoard['botM'] + '|' + tttBoard['botR'])
    print('')


def printMenu():
    print('Welcome to Tic-Tac-Toe!')
    print('Possible moves: ')
    print(' -topL, topM, topR')
    print(' -midL, midM, midR')
    print(' -botL, botM, botR')
    printBoard()


def doAIMove():
    validMove = False
    move = random.randint(0, 8)

    while(validMove == False):
        if tttBoard[tttMoves[move]] == ' ':
            tttBoard[tttMoves[move]] = AI
            validMove = True
        else:
            move = random.randint(0, 8)
        
        

def doPlayerMove():
    valid = False
    position = ''

    while valid == False:
        position = input('Enter a position on the board: ')
        if position in tttBoard.keys() and tttBoard[position] == ' ':
            valid = True
        else:
            print('Invalid Position')

    tttBoard[position] = player


def getPlayerShape():
    valid = False
    shape = ''
    
    while valid == False:
        shape = input('Enter a shape to play (x or o): ')
        if shape not in validShapes:
            print('Invalid shape')
        else:
            valid = True

    return shape


def setAIShape():
    shape = ''

    if player == 'o':
        shape = 'x'
    elif player == 'O':
        shape = 'X'
    elif player == 'x':
        shape = 'o'
    elif player == 'X':
        shape = 'O'

    return shape


def gameLoop():
    gameOver = 0
    printMenu()

    global player
    player = getPlayerShape()

    global AI
    AI = setAIShape()
    
    while gameOver == 0:
        doPlayerMove()
        if winner() == True:
            gameOver = 1
        print(gameOver)
        if gameOver == 0:
            doAIMove()
            if winner() == True:
                gameOver = 2

        printBoard()

    if gameOver == 1:
        print('Congratulations! You Win!')
    else:
        print('You lose')
    

gameLoop()
