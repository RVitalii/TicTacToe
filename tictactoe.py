import sys
from tools import Player, Game

def menuStage():
    print("WELCOME TO TIC-TAC-TOE!!!\n")
    print("### MAIN MENU ###")
    print("1. New Game")
    print("2. Exit")
    print("Press 1-2 to choose your option.")

def TicTacToe():
    menuStage()
    option = input().strip()
    if option == '1':
        gameStage()
    if option == '2':
        exitStage()

def exitStage():
    print('Do you want to exit the game?')
    print('1. Yes')
    print('2. No')
    if input().strip() == '1':
        sys.exit(0)
    else:
        TicTacToe()

def gameCreationStage():
    print('Player 1, please, enter your nickname.')
    player1 = Player(input(), 'X')
    print('Player 2, please, enter your nickname.')
    player2 = Player(input(), 'O')
    game = Game([player1, player2])
    return player1, player2, game

def moveStage(game, player):
            print(game.board)
            print(f'{player.name} is your turn! You are playing for {player.role}.')
            while True:
                try:
                    player.makeMove(game, input())
                    print('') 
                except:
                    continue
                else:
                    break

def endMoveStage(game):
    game.checkGameState()
    if game.isOver:
        print(game.board)
        print(game.results, end = '\n')
        print('Do you want to start a new game?')
        print('1. Yes')
        print('2. No')
        option = input().strip()
        if option == '1':
            game.resetGame()
        else:
            exitStage()

def gameStage():
    player1, player2, game = gameCreationStage()
    while True:
        moveStage(game, player1)
        endMoveStage(game)
        moveStage(game,player2)
        endMoveStage(game)