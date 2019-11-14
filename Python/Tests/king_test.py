# Imports
import sys
sys.path.append('../Pieces')
import king as KING
import rook as ROOK
sys.path.append('../BoardStuff')
import board as BOARD

################################################################################
############################### Castling Test 1 ################################
################################################################################

# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(KING.King(white), 'G', 1)
b_true.set_piece(KING.King(black), 'C', 8)
b_true.set_piece(ROOK.Rook(black), 'H', 8)
b_true.set_piece(ROOK.Rook(black), 'D', 8)
b_true.set_piece(ROOK.Rook(white), 'F', 1)
b_true.set_piece(ROOK.Rook(white), 'A', 1)

#   Test Board
b_test.set_piece(KING.King(white), 'E', 1)
b_test.set_piece(KING.King(black), 'E', 8)
b_test.set_piece(ROOK.Rook(black), 'H', 8)
b_test.set_piece(ROOK.Rook(black), 'A', 8)
b_test.set_piece(ROOK.Rook(white), 'H', 1)
b_test.set_piece(ROOK.Rook(white), 'A', 1)

# Test
true_values = []
test_values = []

# Movement Test for Castling
test_values.append(b_test.move_piece(white, 'E', 1, 'G', 1))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(black, 'E', 8, 'C', 8))  # Move 2
true_values.append(True)


print('-------------------- TRUE 1 ---------------------\n')
b_true.print_board()
print('-------------------- TEST 1 ---------------------\n')
b_test.print_board()

accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])

################################################################################
############################### Castling Test 2 ################################
################################################################################

# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(KING.King(white), 'C', 1)
b_true.set_piece(KING.King(black), 'G', 8)
b_true.set_piece(ROOK.Rook(black), 'F', 8)
b_true.set_piece(ROOK.Rook(black), 'A', 8)
b_true.set_piece(ROOK.Rook(white), 'H', 1)
b_true.set_piece(ROOK.Rook(white), 'D', 1)

#   Test Board
b_test.set_piece(KING.King(white), 'E', 1)
b_test.set_piece(KING.King(black), 'E', 8)
b_test.set_piece(ROOK.Rook(black), 'H', 8)
b_test.set_piece(ROOK.Rook(black), 'A', 8)
b_test.set_piece(ROOK.Rook(white), 'H', 1)
b_test.set_piece(ROOK.Rook(white), 'A', 1)

# Test
true_values = []
test_values = []

# Movement Test for Castling
test_values.append(b_test.move_piece(white, 'E', 1, 'C', 1))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(black, 'E', 8, 'G', 8))  # Move 2
true_values.append(True)


print('-------------------- TRUE 2 ---------------------\n')
b_true.print_board()
print('-------------------- TEST 2 ---------------------\n')
b_test.print_board()

accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])

################################################################################
############################### Castling Test 3 ################################
################################################################################

# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(KING.King(white), 'E', 1)
b_true.set_piece(KING.King(black), 'E', 8)
b_true.set_piece(ROOK.Rook(black), 'H', 8)
b_true.set_piece(ROOK.Rook(black), 'A', 8)
b_true.set_piece(ROOK.Rook(white), 'H', 1)
b_true.set_piece(ROOK.Rook(white), 'A', 1)

#   Test Board
b_test.set_piece(KING.King(white), 'E', 1)
b_test.set_piece(KING.King(black), 'E', 8)
b_test.set_piece(ROOK.Rook(black), 'H', 8)
b_test.set_piece(ROOK.Rook(black), 'A', 8)
b_test.set_piece(ROOK.Rook(white), 'H', 1)
b_test.set_piece(ROOK.Rook(white), 'A', 1)
# white king has already moved
b_test.grid[7][4].piece.turn_last_moved = 10
# black rooks have already moved
b_test.grid[0][0].piece.turn_last_moved = 10
# white king has already moved
b_test.grid[0][7].piece.turn_last_moved = 10

# Test
true_values = []
test_values = []

# Movement Test for Castling
test_values.append(b_test.move_piece(white, 'E', 1, 'C', 1))  # Move 1
true_values.append(False)
test_values.append(b_test.move_piece(black, 'E', 8, 'G', 8))  # Move 2
true_values.append(False)


print('-------------------- TRUE 3 ---------------------\n')
b_true.print_board()
print('-------------------- TEST 3 ---------------------\n')
b_test.print_board()

accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])

################################################################################
############################### Castling Test 4 ################################
################################################################################

# Copy previous castling test, check for castling through check

################################################################################
############################# General King Test 5 ##############################
################################################################################

# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(KING.King(white), 'E', 1)
b_true.set_piece(KING.King(black), 'E', 8)
b_true.set_piece(ROOK.Rook(black), 'H', 8)
b_true.set_piece(ROOK.Rook(black), 'A', 8)
b_true.set_piece(ROOK.Rook(white), 'H', 1)
b_true.set_piece(ROOK.Rook(white), 'A', 1)

#   Test Board
b_test.set_piece(KING.King(white), 'D', 1)
b_test.set_piece(KING.King(black), 'E', 8)
b_test.set_piece(ROOK.Rook(black), 'H', 8)
b_test.set_piece(ROOK.Rook(black), 'A', 8)
# white king has already moved
b_test.grid[7][3].piece.turn_last_moved = 10

# Test
true_values = []
test_values = []

# Movement Test for Castling
test_values.append(b_test.move_piece(white, 'D', 1, 'D', 3))  # Move 1
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 1, 'D', 0))  # Move 2
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 1, 'C', 2))  # Move 3
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 2, 'B', 3))  # Move 4
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 3, 'B', 4))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 4, 'A', 4))  # Move 6 Moving into Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 4, 'B', 4))  # Move 7 Moving out of previous False Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'B', 4, 'C', 5))  # Move 8
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 5, 'D', 5))  # Move 9
true_values.append(True)
test_values.append(b_test.move_piece(white, 'D', 5, 'E', 6))  # Move 10
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 6, 'E', 7))  # Move 11 Moving into Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'E', 7, 'E', 6))  # Move 12 Moving out of previous False Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'E', 6, 'F', 6))  # Move 13
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 6, 'G', 7))  # Move 14
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 7, 'H', 7))  # Move 15 Moving into Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'H', 7, 'G', 7))  # Move 16 Moving out of previous False Check
true_values.append(False)
test_values.append(b_test.move_piece(white, 'G', 7, 'H', 8))  # Move 17
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 8, 'H', 9))  # Move 18
true_values.append(False)
test_values.append(b_test.move_piece(white, 'H', 8, 'I', 8))  # Move 19
true_values.append(False)
test_values.append(b_test.move_piece(white, 'H', 8, 'H', 7))  # Move 20
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 7, 'G', 6))  # Move 21
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 6, 'F', 6))  # Move 22
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 6, 'G', 5))  # Move 23
true_values.append(True)
test_values.append(b_test.move_piece(black, 'A', 8, 'A', 5))  # Move 24
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 5, 'G', 4))  # Move 25
true_values.append(True)


print('-------------------- TRUE 5 ---------------------\n')
b_true.print_board()
print('-------------------- TEST 5 ---------------------\n')
b_test.print_board()

accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])
