import pprint
import random

tttBoard = {'topL':' ', 'topM':' ', 'topR':' ',
            'midL':' ', 'midM':' ', 'midR':' ',
            'botL':' ', 'botM':' ', 'botR':' '};

validShapes = ['X', 'x', 'O', 'o'];


def winner():
    if tttBoard['topL'] in validShapes:
        if tttBoard['topL'] == tttBoard['topM'] == tttBoard['topR']:
            return True;
        elif tttBoard['topL'] == tttBoard['midM'] == tttBoard['botR']:
            return True;
        elif tttBoard['topL'] == tttBoard['midL'] == tttBoard['botL']:
            return True;
    elif tttBoard['topM'] in validShapes:
        if tttBoard['topM'] == tttBoard['midM'] == tttBoard['botm']:
            return True;
    elif tttBoard['topR'] in validShapes:
        if tttBoard['topR'] == tttBoard['midR'] == tttBoard['botR']:
            return True;
        elif tttBoard['topR'] == tttBoard['midM'] == tttBoard['botL']:
            return True;
    elif tttBoard['midL'] in validShapes:
        if tttBoard['midL'] == tttBoard['midM'] == tttBoard['midR']:
            return True;
    elif tttBoard['botL'] in validShapes:
        if tttBoard['botL'] == tttBoard['botM'] == tttBoard['botR']:
            return True;    

    return False;


def printBoard():
    print('');
    print(tttBoard['topL'] + '|' + tttBoard['topM'] + '|' + tttBoard['topR']);
    print('------');
    print(tttBoard['midL'] + '|' + tttBoard['midM'] + '|' + tttBoard['midR']);
    print('------');
    print(tttBoard['botL'] + '|' + tttBoard['botM'] + '|' + tttBoard['botR']);
    print('');


def printMenu():
    print('Welcome to Tic-Tac-Toe!');
    print('Possible moves: ');
    print(' -topL, topM, topR');
    print(' -midL, midM, midR');
    print(' -botL, botM, botR');
    printBoard();


def getPlayerInput():
    valid = False;
    position = '';
    shape = '';

    while valid == False:
        if position in tttBoard.keys() and tttBoard[position] == ' ':
            valid = True;
        else:
            position = input('Enter a position on the board: ');

    valid = False;

    while valid == False:
        if shape in validShapes:
            valid = True;
        else:
            shape = input('Enter a shape (X or O): ');

    tttBoard[position] = shape;

    

def gameLoop():
    player = 'person';
    gameOver = False;

    printMenu();
    
    while gameOver == False:
        getPlayerInput();
        if winner() == True:
            gameOver = True;

        printBoard();

    print('Game Over');
    

gameLoop();
