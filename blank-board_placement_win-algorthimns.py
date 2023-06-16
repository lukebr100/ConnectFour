import random

 # col_count[i] represents the number of times a player has placed a stone in column i, i = 0, 1, ..., 6
col_count = [0 for i in range(7)]







def valid_choice(i):                                     
    if isinstance(i, int) and 0 <= i <= 6:            
        return True                         
    else:
        return False                      
        
def col_limit(x):
    for i in range(7):
        if x.count(i) > 6:
            return False
    return True

def turn_limit(x):
    if len(x) < 42:
        return True
    else:
        return False


def turn_and_col_lim(x):
    if turn_limit(x) == True and col_limit(x) == True:
        return True
    else:
        return False



def turn_col_valid_choice(x, i):
    if turn_and_col_lim(x) == True and valid_choice(i) == True:
        return True
    else:
        return False


def next_pos_valid(x, i):
    if valid_choice(i) == True and turn_and_col_lim(x + [i]) == True:
        return True
    else:
        return False


def whose_turn(turn_num, player):      
    if turn_num % 2 == 0:
        return player[0]
    if turn_num % 2 == 1:
        return player[1]

# initial column choices [0, 1, ..., 6]
z = [i for i in range(7)]

# initial turn num
turn_num = 0

# intital pos seq
x = []

def players(start):
    if 'play' in x:
        player1 = input('player 1 choose any character: ')
        player2 = input('player 2 choose any character: ')
        player = [player1, player2]
        return player

def user_game(blank):
    print('type play')  
    start = input()
    players(start)
    print(player)
    
    turn_num = 0
    x = []
    z = [i for i in range(7)]

    while turn_limit(x) == True:
        whose_turn(turn_num, player)
        pos_seq = pos_seq + [x]
        board[5 - col_count[x]][x] = turn(turn_num, 'L', 'K')
        turn_num = turn_num + 1
        col_count[x] = col_count[x] + 1
        parity = parity + 1

        print(pos_seq)
        print(col_count)
        print(turn_num)
        print_board(board)
        

    
    return place(board, turn_num, parity, pos_seq)






    
