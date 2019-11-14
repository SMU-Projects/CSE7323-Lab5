# Imports
import sys
sys.path.append('../Pieces')
import rook as ROOK
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(ROOK.Rook(white), 'E', 7)
b_true.set_piece(ROOK.Rook(white), 'H', 8)

#   Test Board
b_test.has_king = False
b_test.set_piece(ROOK.Rook(white), 'A', 1)
b_test.set_piece(ROOK.Rook(black), 'H', 1)
b_test.set_piece(ROOK.Rook(black), 'A', 8)
b_test.set_piece(ROOK.Rook(white), 'H', 8)


# Test
true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'A', 1, 'A', 2))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 2, 'A', 8))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 1, 'A', 8))  # Move 3
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 8, 'H', 8))  # Move 4
true_values.append(False)
test_values.append(b_test.move_piece(black, 'H', 1, 'D', 1))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(black, 'D', 1, 'D', 8))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 8, 'F', 8))  # Move 7
true_values.append(False)
test_values.append(b_test.move_piece(black, 'D', 8, 'D', 7))  # Move 8
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 8, 'A', 7))  # Move 9
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 7, 'D', 7))  # Move 10
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 8, 'A', 1))  # Move 11
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 7, 'B', 8))  # Move 12
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 7, 'E', 7))  # Move 13
true_values.append(True)

print('-------------------- TRUE ---------------------\n')
b_true.print_board()
print('-------------------- TEST ---------------------\n')
b_test.print_board()


accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1,'--- truth:', true_values[i], '||| test:',test_values[i])
