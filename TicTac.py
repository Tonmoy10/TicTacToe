import math
import copy

max_player = 'X'
min_player = 'O'


def player(player):  #[Return the next player]
    if player=='X':
        player = 'O'
    else:
        player = 'X'
        
    return player


def actions(state):   #[Return a list that contains the index number(row, column) of the empty positions in the current state.]
    actionList = []
    for r in range(0,3):
        for c in range(0,3):
            if state[r][c] == '-':
                actionList.append((r,c))
    return actionList


def result(state, action, player):          
    state[action[0]][action[1]] = player
    return state

def terminal(state):    #[If terminal then return True Otherwise Return False]
    
    #Row and Column Check
    for i in range(0,3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '-':
            return True
        elif state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            return True
    
    #Diagonal Check
    if  state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        return True
    elif state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        return True
    
    #Draw Check
    isTerminal = True
    for row in state:
        for item in row:
            if item == '-':
                isTerminal = False
    
    return isTerminal
    

def utility(state): #[Return the utility value(1,0,-1) of a terminal state]
    player = ''
    #Row and Column Check
    for i in range(0,3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '-':
            player = state[i][0]
        elif state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            player = state[0][i]
    
    #Diagonal Check
    if  state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        player = state[0][0]
    elif state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        player = state[0][2]
  
    
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    
    player = 'Draw'
    #Draw Check
    for row in state:
        for item in row:
            if item == '-':
                player = 'Error::Not a Terminal State'
    

    if player == 'Draw':
        return 0
    else:
        return player



def max_value(state):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v,min_value(result(copy.deepcopy(state),action,max_player)))
    return v


def min_value(state):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v,max_value(result(copy.deepcopy(state),action,min_player)))
    return v




def printBoard(board):
    for row in board:
        print(row)
            


def tic_tac_toe():

    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
    #plr = max_player
    #Implement this function
    print("______________Welcome to the game of Tic Tac Toe_______________\n")
    plr = input("Select a player\n1. X\n2. O\nANSWER : ")
    if(plr == 'X' or plr == 'x' or plr == '1'):
        plr = max_player
        while True:
            printBoard(board)
            print ("\n")
            if(plr==max_player):
                r = int(input("Enter row: "))
                c = int(input("Enter column: "))
                tup = (r,c)
                result(board,tup,plr)
                
                if terminal(board):
                    final = utility(board)
                    if final == 1:
                        printBoard(board)
                        print("Human has won")
                    elif final == -1:
                        printBoard(board)
                        print("AI has won")
                    elif final == 0:
                        printBoard(board)
                        print("Draw")
                    return
                plr = player(plr)
            elif(plr == min_player):
                flg = 10
                for move in actions(board):
                    res = min_value(result(copy.deepcopy(board),move,plr))
                    if res == -1:
                        result(board,move,plr)
                        flg=1
                        break
                
                for move in actions(board):
                    res = min_value(result(copy.deepcopy(board),move,plr))
                    if res == 0 and flg != 1:
                        result(board,move,plr)
                        flg=2
                        break
                
                for move in actions(board):
                    res = min_value(result(copy.deepcopy(board),move,plr))
                    if res == 1 and flg != 1 and flg != 2:
                        result(board,move,plr)
                        flg=0
                        break
                
                
                
                if terminal(board):
                    final = utility(board)
                    if final == 1:
                        printBoard(board)
                        print("Human has won")
                    elif final == -1:
                        printBoard(board)
                        print("AI has won")
                    elif final == 0:
                        print("Draw")
                        printBoard(board)
                        
                    
                    return
                    
                plr = player(plr)
    elif(plr == 'O' or plr == 'o' or plr == '2'):
        plr = max_player
        while True:
            printBoard(board)
            print ("\n")
            if(plr==min_player):
                r = int(input("Enter row: "))
                c = int(input("Enter column: "))
                tup = (r,c)
                result(board,tup,plr)
                
                if terminal(board):
                    final = utility(board)
                    if final == -1:
                        printBoard(board)
                        print("Human has won")
                    elif final == 1:
                        printBoard(board)
                        print("AI has won")
                    elif final == 0:
                        printBoard(board)
                        print("Draw")
                    return
                plr = player(plr)
            if(plr == max_player):
                flg = 10
                for move in actions(board):
                    res = max_value(result(copy.deepcopy(board),move,plr))
                    if res == 1:
                        result(board,move,plr)
                        flg = 1
                        break
                
                for move in actions(board):
                    res = min_value(result(copy.deepcopy(board),move,plr))
                    if res == 0 and flg != 1:
                        result(board,move,plr)
                        flg=2
                        break
                
                for move in actions(board):
                    res = min_value(result(copy.deepcopy(board),move,plr))
                    if res == -1 and flg != 1 and flg != 2:
                        result(board,move,plr)
                        flg = 0
                        break
                
                
                
                if terminal(board):
                    final = utility(board)
                    if final == -1:
                        printBoard(board)
                        print("Human has won")
                    elif final == 1:
                        printBoard(board)
                        print("AI has won")
                    elif final == 0:
                        print("Draw")
                        printBoard(board)
                        
                    
                    return
                    
                plr = player(plr)
    else:
        print("Invalid Input!!")
tic_tac_toe()
    
    
    
    
    
    
1