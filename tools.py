from math import ceil

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

class Board:
    
    def __init__(self, size):
        self.size = int(2 * size - 1)
        self.board = [[None for _ in range(self.size)] for _ in range(self.size+1)]
        self.__cell_len = len(str((ceil(self.size / 2) * ceil(self.size / 2)))) + 3
        self.__boardElements = [' ' * self.__cell_len, 
                              '_'  * self.__cell_len, 
                              '|', 
                              'X' + ' ' * (self.__cell_len-1), 
                              'O' + ' ' * (self.__cell_len-1)]

    def __repr__(self):
        return f"board({self.size})"

    def __str__(self):
        out = ''
        for row in self.board:
            out += ''.join(row) + '\n'
        return out

    def createBoard(self):
        for i in range(self.size+1):
            for j in range(self.size):
                if i != self.size:
                    if isEven(i) and isEven(j):
                            row = i // 2 
                            col = j // 2 + 1
                            num = str(row * ceil(self.size / 2) + col)
                            self.board[i][j] = num + ' ' * (self.__cell_len - len(num))
                    if isEven(i) and not isEven(j):
                        self.board[i][j] = self.__boardElements[2]
                    if not isEven(i) and isEven(j):
                        self.board[i][j] = self.__boardElements[1]
                    if not isEven(i) and not isEven(j):
                        self.board[i][j] = self.__boardElements[2]
                else:
                    if isEven(j):
                        self.board[i][j] = self.__boardElements[0]
                    else: 
                        self.board[i][j] = self.__boardElements[2]               

    def positionToCoordinates(self, pos):
        pos = int(pos)
        row = (pos-1) // ceil(self.size / 2) * 2  
        col = (pos-1) % ceil(self.size / 2) * 2
        return row, col
    
    def mark(self, pos, type):
        row, col = self.positionToCoordinates(pos)
        if type == 'X':
            self.board[row][col] = self.__boardElements[3]
        elif type == 'O':
            self.board[row][col] = self.__boardElements[4]
        else:
            raise ValueError('Invalid type.')        

class Player:
    
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"Game{self.name, self.role}"

    def makeMove(self, game, pos):
        if game.isCellLocked(pos):
            print(f'Oops, it seems cell {pos} is locked. Please, try again!')
            raise Exception
        else:
            game.board.mark(pos, self.role)
            game.lockedCells += [int(pos)]
            row, col = game.board.positionToCoordinates(pos)
            game.visitedRows[self.name][row // 2] += 1
            game.visitedColumns[self.name][col // 2] += 1

class Game:

    def __init__(self, players):
        if len(players) == 2:
            self.players = players
        else:
            raise ValueError('There must be 2 players in a game!')
        self.board = Board(3)
        self.board.createBoard()
        self.isOver = False
        self.results = 'Tie!'
        self.lockedCells = [] 
        self.visitedRows = dict(zip([player.name for player in players], [[0,0,0] for _ in players]))
        self.visitedColumns = dict(zip([player.name for player in players], [[0,0,0] for _ in players]))

    def __repr__(self):
        return f"Game({self.name})"
    
    def resetGame(self):
        self.board.createBoard()
        self.isOver = False
        self.results = 'Tie!'
        self.lockedCells = [] 
        self.visitedRows = dict(zip([player.name for player in self.players], [[0,0,0] for _ in self.players]))
        self.visitedColumns = dict(zip([player.name for player in self.players], [[0,0,0] for _ in self.players]))

    def isCellLocked(self, pos):
        return int(pos) in self.lockedCells
    
    def checkGameState(self):
       for player in self.players:
        allConditions = sum(self.visitedRows.values(), []) + sum(self.visitedColumns.values(), [])
        allPlayersConditions = self.visitedRows[player.name] + self.visitedColumns[player.name]
        if sum(allConditions) == 18:
            self.isOver = True
        if 3 in allPlayersConditions:
            self.isOver = True
            self.results = f'{player.name} has won!'
        if sum([condition == 1 for condition in allPlayersConditions]) == 6:
            self.isOver = True
            self.results = f'{player.name} has won!'