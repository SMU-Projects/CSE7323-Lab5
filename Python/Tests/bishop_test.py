# Imports
import sys
sys.path.append('../Pieces')
import bishop as BISHOP
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(BISHOP.Bishop(white), 'A', 8)
b_true.set_piece(BISHOP.Bishop(black), 'B', 1)
b_true.set_piece(BISHOP.Bishop(white), 'H', 7)
b_true.set_piece(BISHOP.Bishop(black), 'F', 7)

#   Test Board
b_test.has_king = False
b_test.set_piece(BISHOP.Bishop(white), 'D', 5)
b_test.set_piece(BISHOP.Bishop(black), 'C', 6)
b_test.set_piece(BISHOP.Bishop(black), 'H', 1)
b_test.set_piece(BISHOP.Bishop(white), 'A', 8)
b_test.set_piece(BISHOP.Bishop(black), 'H', 7)
b_test.set_piece(BISHOP.Bishop(white), 'B', 1)
b_test.set_piece(BISHOP.Bishop(white), 'G', 8)
b_test.set_piece(BISHOP.Bishop(black), 'D', 7)


# Test
true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'D', 5, 'B', 7))  # Move 1
true_values.append(False)
test_values.append(b_test.move_piece(black, 'D', 5, 'H', 1))  # Move 2
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 5, 'H', 1))  # Move 3
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 6, 'H', 1))  # Move 4
true_values.append(False)
test_values.append(b_test.move_piece(black, 'C', 6, 'H', 1))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 8, 'H', 1))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 1, 'A', 8))  # Move 7
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 7, 'B', 1))  # Move 8
true_values.append(False)
test_values.append(b_test.move_piece(black, 'H', 7, 'B', 1))  # Move 9
true_values.append(True)
test_values.append(b_test.move_piece(black, 'H', 1, 'A', 8))  # Move 10
true_values.append(False)
test_values.append(b_test.move_piece(white, 'G', 8, 'F', 7))  # Move 11
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 7, 'G', 8))  # Move 12
true_values.append(True)
test_values.append(b_test.move_piece(black, 'D', 7, 'E', 6))  # Move 13
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 8, 'D', 5))  # Move 14
true_values.append(False)
test_values.append(b_test.move_piece(white, 'G', 8, 'H', 7))  # Move 15
true_values.append(True)
test_values.append(b_test.move_piece(black, 'E', 6, 'F', 7))  # Move 16
true_values.append(True)
test_values.append(b_test.move_piece(black, 'B', 1, 'D', 1))  # Move 17
true_values.append(False)
test_values.append(b_test.move_piece(black, 'B', 1, 'B', 1))  # Move 18
true_values.append(False)
test_values.append(b_test.move_piece(black, 'B', 1, 'B', 3))  # Move 19
true_values.append(False)
test_values.append(b_test.move_piece(black, 'H', 7, 'F', 7))  # Move 20
true_values.append(False)



print('-------------------- TRUE ---------------------\n')
b_true.print_board()
print('-------------------- TEST ---------------------\n')
b_test.print_board()


accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])
