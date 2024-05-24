#Tick Tack Toe

import random

def draawBoard(board):
    #this is a function that prints out the board that it was paassed

    #"board is a list of 10 strings representing the board(ignore index0).

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[1])

def inputPlayerLetter():
    #lets the player type  Whitch letter they want to be.
    #Returns a list with the player's letter as the first item in the computer's letter as the second.
    letter = ''
    while not (letter = 'X' or letter == 'O'):
        print ('Do you want to be X or O')
        letter = input().upper()
        # the first elemnt in the list is the players letter; the second is the computers letter.
        if letter == 'X':
            return['X','O']
        else:
            return['O','X']

def whoGoesFirst():
    #Randomly choose , which player goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def isWinner(bo,le):
    ##given a board and a players letter this function returns true if that plyer has won.
    #we use "bo" instead of "boaard" and "le" instead of letter so we caan saave time.
    return((bo[7] == le and bo[8] == le and bo[9] == le) or #across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # middle win
    (bo[1] == le and bo[2] == le and bo[3] == le) or #bottom row win
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down left win
    (bo[8] == le and bo[5] == le and bo[2] == le) or # win down middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # in down right
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal 1
    (bo[9] == le and bo[5] == le and bo[1] == le)) #diaagonal 2

def getBoardCopy(board):
    #make a coppy of bord and return
    boardCoppy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board):
    #
