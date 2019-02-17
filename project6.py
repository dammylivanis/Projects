import random


class square(object):
    value = 0
    selected = False
    mine = False

    def __init__(self):
        self.selected = False

    def __str__(self):
        return str(boardSpot.value)

    def isMine(self):
        if boardSpot.value == -1:
            return True
        return False


class table(object):
    def __init__(self, iboardsize, numminess):
        self.board = [[square() for i in range(iboardsize)] for j in range(iboardsize)]
        self.boardSize = iboardsize
        self.numMines = numminess
        self.selectableSpots = iboardsize * iboardsize - numminess
        i = 0
        while i < numminess:
            x = random.randint(0, self.boardSize-1)
            y = random.randint(0, self.boardSize-1)
            if not self.board[x][y].mine:
                self.mine(x, y)
                i += 1
            else:
                i -= 1

    def __str__(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.boardSize):
            returnString += " | " + str(i)
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.boardSize):
            returnString += str(y)
            for x in range(0, self.boardSize):
                if self.board[x][y].mine and self.board[x][y].selected:
                    returnString += " |" + str(self.board[x][y].value)
                elif self.board[x][y].selected:
                    returnString += " | " + str(self.board[x][y].value)
                else:
                    returnString += " |  "
            returnString += " |"
            returnString += divider
        return returnString

    def mine(self, x, y):
        self.board[x][y].value = -1
        self.board[x][y].mine = True
        for i in range(x-1, x+2):
            if i >= 0 and i < self.boardSize:
                if y-1 >= 0 and not self.board[i][y-1].mine:
                    self.board[i][y-1].value += 1
                if y+1 < self.boardSize and not self.board[i][y+1].mine:
                    self.board[i][y+1].value += 1
        if x-1 >= 0 and not self.board[x-1][y].mine:
            self.board[x-1][y].value += 1
        if x+1 < self.boardSize and not self.board[x+1][y].mine:
            self.board[x+1][y].value += 1

    def move(self, x, y):
        self.board[x][y].selected = True
        self.selectableSpots -= 1
        if self.board[x][y].value == -1:
            return False
        if self.board[x][y].value == 0:
            for i in range(x-1, x+2):
                if i >= 0 and i < self.boardSize:
                    if y-1 >= 0 and not self.board[i][y-1].selected:
                        self.move(i, y-1)
                    if y+1 < self.boardSize and not self.board[i][y+1].selected:
                        self.move(i, y+1)
            if x-1 >= 0 and not self.board[x-1][y].selected:
                self.move(x-1, y)
            if x+1 < self.boardSize and not self.board[x+1][y].selected:
                self.move(x+1, y)
            return True
        else:
            return True

    def hitm(self, x, y):
        return self.board[x][y].value == -1

    def Winner(self):
        return self.selectableSpots == 0


def play():
    boardSize = int(input("Choose the Width of the board: "))
    numMines = int(input("Choose the number of mines: "))
    gameOver = False
    winner = False
    tablegame = table(boardSize, numMines)
    while not gameOver:
        print(tablegame)
        print("Make your move:")
        x = int(input("x: "))
        y = int(input("y: "))
        tablegame.move(x, y)
        gameOver = tablegame.hitm(x, y)
        if tablegame.Winner() and gameOver == False:
            gameOver = True
            winner = True
    print(tablegame)
    if winner:
        print("Congratulations, You Won!")
    else:
        print("You hit a mine, Game Over!")
play()
