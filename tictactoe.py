from tools import Player, Game

def TicTacToe():
    print("WELCOME TO TIC-TAC-TOE!!!\n")
    print("### MAIN MENU ###")
    print("1. New Game")
    print("2. Exit\n")
    print("Press 1-2 to choose your option.\n")
    option = input().strip()
    print('')
    
    if option == '1':
        print('Player 1, please, enter your nickname.\n')
        player1 = Player(input(), 'X')
        print('')
        print('Player 2, please, enter your nickname.\n')
        player2 = Player(input(), 'O')
        print('')
        game = Game([player1, player2])
        while True:
            print(game.board)
            print(f'{player1.name} is your turn! You are playing for {player1.role}.')
            while True:
                try:
                    player1.makeMove(game, input())
                    print('') 
                except:
                    continue
                else:
                    break           
            game.checkGameState()
            if game.isOver:
                print(game.board)
                print(game.results)
                break
            print(game.board)
            print(f'{player2.name} is your turn! You are playing for {player2.role}.')
            while True:
                try:
                    player2.makeMove(game, input())
                    print('')  
                except:
                    continue
                else:
                    break  
            game.checkGameState()
            if game.isOver:
                print(game.board)
                print(game.results)
                print('Do you want to start a new game?')
                print('1. Yes')
                print('2. No')
                if input().split() == '1':
                    game.resetGame()
                else:
                    break

    if option == '2':
        pass