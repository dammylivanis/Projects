import random

def createboard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def playersletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choose you letter: X or O !')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def firsttoplay():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def dmove(board, letter, move):
    board[move] = letter

def winner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def copyboard(board):
    dBoard = []

    for i in board:
        dBoard.append(i)

    return dBoard

def freespace(board, move):
    return board[move] == ' '

def rng(board, movesList):
    possibleMoves = []
    for i in movesList:
        if freespace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def moveplayer(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freespace(board, int(move)):
        print('What is your move?')
        move = input()
    return int(move)


def movecomp(board, computerLetter):
 if computerLetter == 'X':
    playerLetter = 'O'
 else:
    playerLetter = 'X'

 act = True
 while act:
  move = random.randint(0,9)
  if freespace(board,move):
     act = False
     return move


def fullboard(board):
 for i in range(1, 10):
  if freespace(board,i):
    return False
 return True


print("Let's play Tic Tac Toe!")

while True:

    theBoard = [' '] * 10
    playerLetter, computerLetter = playersletter()
    turn = firsttoplay()
    print('The ' + turn + ' will go first.')
    play = True

    while play:
        if turn == 'player':
            print('Your Turn!')
            print('Choose numbers from 1-9.The game goes like this : First line : 1 | 2 | 3 . Second line: 4 | 5 |6 .Third line: 7 | 8 | 9  .')
            createboard(theBoard)
            move = moveplayer(theBoard)
            dmove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                createboard(theBoard)
                print(' You win!')
                play = False
            else:
                if fullboard(theBoard):
                    createboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            print("Computer's Turn!")
            move = movecomp(theBoard, computerLetter)
            dmove(theBoard, computerLetter, move)
            createboard(theBoard)
            if winner(theBoard, computerLetter):
                createboard(theBoard)
                print('Computer wins')
                play = False
            else:
                if fullboard(theBoard):
                    createboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    break
