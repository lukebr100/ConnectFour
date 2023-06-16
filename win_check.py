from blank_board import blank
from row_CF import row
from column_CF import column
from print_matrix import print_matrix


board = blank('y')
# calls blank from blank_board.py stores in var. board
# print_matrix(board)
# prints var. board
# print(board[5][0:4])
# prints the bottom row first four columns of board
# print(row(board, 5)[0:4])
# same as above?  can't tell b/c all entries are zero! but i think its the same position as above
# which method is better?


# input: board arrangement, row i, mark - player's character
# output: does player mark wins at that position?
def horizontal_win_chk(board, i, mark):
    win = [mark, mark, mark, mark]
    row_i = row(board, i)
    for k in range(4):
        if row_i[k:k + 4] == win:
            return True, mark, 'wins'
    
def vertical_win_chk(board, i, mark):
    win = [mark, mark, mark, mark]
    col_i = column(board, i)
    for k in range(4):
        if col_i[k:k + 4] == win:
            return True, mark, 'wins'
        


# intialize and print test board
board0 = [[i for i in range(k, k + 7)] for k in range(0, 37, 7)]
print_matrix(board0)
print('board0')

board1 = board0[:]
board1[5][0:4] = ['L', 'L', 'L', 'L']
    
print_matrix(board1)
print('board1')

print_matrix(board0)
print('board0 overwritten with board1')             ### help

board2 = board0.copy()
for i in range(2,6):
    board2[i][0] = 'L'
print_matrix(board2)
print('board2')
# board1 operation modified board0 when I wrote board1 = board0
# using board1 = board0.copy() or board1 = board0[:] (slicing) should handle it
# but it does not



# input: does player mark have horizontal/vert win in any row/col
# output: only if player x win via horizontally/vert

def hor_all_win_chk(board, mark):
    for i in range(6):
        if horizontal_win_chk(board, i, mark)[0] == True:
            return True, mark, 'wins'

def vert_all_win_chk(board, mark):
    for i in range(7):
        if vertical_win_chk(board, i, mark)[0] == True:
            return True, mark, 'wins'