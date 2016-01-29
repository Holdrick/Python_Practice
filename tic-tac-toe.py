import pprint
import random

tttBoard = {'topL':'', 'topM':'', 'topR':'',
            'midL':'', 'midM':'', 'midR':'',
            'botL':'', 'botM':'', 'botR':''};

validShapes = ['X', 'x', 'O', 'o'];

def printBoard():
    print('');
    print(tttBoard['topL'] + ' | ' + tttBoard['topM'] + ' | ' + tttBoard['topR']);
    print('------');
    print(tttBoard['midL'] + ' | ' + tttBoard['midM'] + ' | ' + tttBoard['midR']);
    print('------');
    print(tttBoard['botL'] + ' | ' + tttBoard['botM'] + ' | ' + tttBoard['botR']);
    print('');


def printMenu():
    print('Welcome to Tic-Tac-Toe!');
    print('Possible moves: ');
    print(' -topL, topM, topR');
    print(' -midL, midM, midR');
    print(' -botL, botM, botR');
    printBoard();


def getPlayerInput():
    valid = false;
    position = '';
    shape = '';

    while valid == false:
        if position in tttBoard.keys() && tttBoard[position] == '':
            valid = true;
        else:
            position = input('Enter a position on the board: ');

    valid = false;

    while valid == false:
        if shape in validShapes:
            valid = true;
        else:
            shape = input('Enter a shape (X or O): ');

    tttBoard[position] = shape;


def winner():
    

# def gameLoop():
    


printMenu();
# printBoard();
