# Imports
import sys
sys.path.append('../Pieces')
import queen as QUEEN
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(QUEEN.Queen(white), 'F', 7)

#   Test Board
b_test.has_king = False
b_test.set_piece(QUEEN.Queen(white), 'E', 5)
b_test.set_piece(QUEEN.Queen(black), 'A', 2)
b_test.set_piece(QUEEN.Queen(black), 'H', 7)


# Test
true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'E', 5, 'B', 8))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 8, 'A', 8))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 8, 'A', 1))  # Move 3
true_values.append(False)
test_values.append(b_test.move_piece(white, 'A', 8, 'A', 2))  # Move 4
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 2, 'B', 1))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(white, 'B', 1, 'H', 7))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 7, 'F', 7))  # Move 7
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
