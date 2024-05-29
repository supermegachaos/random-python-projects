#Tick Tack Toe

import random

def drawBoard(board):
    #this is a function that prints out the board that it was paassed

    #"board is a list of 10 strings representing the board(ignore index0).

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    #lets the player type  Witch letter they want to be.
    #Returns a list with the player's letter as the first item in the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print ('Do you want to be X or O')
        letter = input().upper()
        # the first elemnt in the list is the players letter; the second is the computers letter.
        if letter == 'X':
            return ['X','O']
        else:
            return ['O','X']

def makeMove(board, letter, move):
    board[move] = letter

def whoGoesFirst():
    #Randomly choose , which player goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def isWinner(bo,le):
    ##given a board and a players letter this function returns true if that plyer has won.
    #we use "bo" instead of "boaard" and "le" instead of letter so we can save time.
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
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    #return true if the passed move is free on the paassed board.
    return board [move] == ' '

def getPlayerMove(board):
    #let the player enter their move.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move? (1-9)')
        move = input()
        return int(move)

def chooseRandomMoveFromList(board, movesList):
    #returns a random move from the list of valid moves, could also do nothing if their are no more moves
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i ):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove (board, computerLetter):
    #given a board and the computer's letter determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter= 'O'
    else:
        playerLetter= 'X'
        # this is the algorithm for our tic-taac-toe AI:, first we check if we can win in the next move.
    for i in range (1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    ##Chech if the player can win on their next move and block them.
    for i in range (1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy,playerLetter, i)
            if isWinner(boardCopy,playerLetter):
                return i
        
    #try the corners
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    #try to take the center
    if isSpaceFree(board,5):
        return 5
    #move to one of the sides.
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #return true if all take otherwise give false
    for i in range (1,10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic-Tac-Toe!')

while True:
    #reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter, move)


            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is  tie!')
                else:
                    turn = 'computer'
        else:
            #CPU turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('the computer has beaten you! You lose. The world is doomed! All hail our robot overloards!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
