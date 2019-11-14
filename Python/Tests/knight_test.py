# Imports
import sys
sys.path.append('../Pieces')
import knight as KNIGHT
sys.path.append('../BoardStuff')
import board as BOARD


# Variables
white = 'white'
black = 'black'
b_true = BOARD.Board()
b_test = BOARD.Board()

# Set Boards
#   True Board
b_true.set_piece(KNIGHT.Knight(black), 'B', 6)
b_true.set_piece(KNIGHT.Knight(black), 'G', 3)
b_true.set_piece(KNIGHT.Knight(white), 'E', 5)  # Selected Knight
b_true.set_piece(KNIGHT.Knight(white), 'E', 6)
b_true.set_piece(KNIGHT.Knight(white), 'E', 4)
b_true.set_piece(KNIGHT.Knight(white), 'D', 5)
b_true.set_piece(KNIGHT.Knight(white), 'F', 5)
b_true.set_piece(KNIGHT.Knight(white), 'E', 7)
b_true.set_piece(KNIGHT.Knight(white), 'E', 3)
b_true.set_piece(KNIGHT.Knight(white), 'C', 5)
b_true.set_piece(KNIGHT.Knight(white), 'G', 5)
b_true.set_piece(KNIGHT.Knight(white), 'D', 6)
b_true.set_piece(KNIGHT.Knight(white), 'F', 6)
b_true.set_piece(KNIGHT.Knight(white), 'D', 4)
b_true.set_piece(KNIGHT.Knight(white), 'F', 4)
b_true.set_piece(KNIGHT.Knight(white), 'C', 4)

#   Test Board
b_test.has_king = False
b_test.set_piece(KNIGHT.Knight(black), 'A', 8)
b_test.set_piece(KNIGHT.Knight(black), 'H', 1)
b_test.set_piece(KNIGHT.Knight(white), 'E', 5)  # Selected Knight
b_test.set_piece(KNIGHT.Knight(white), 'E', 6)
b_test.set_piece(KNIGHT.Knight(white), 'E', 4)
b_test.set_piece(KNIGHT.Knight(white), 'D', 5)
b_test.set_piece(KNIGHT.Knight(white), 'F', 5)
b_test.set_piece(KNIGHT.Knight(white), 'E', 7)
b_test.set_piece(KNIGHT.Knight(white), 'E', 3)
b_test.set_piece(KNIGHT.Knight(white), 'C', 5)
b_test.set_piece(KNIGHT.Knight(white), 'G', 5)
b_test.set_piece(KNIGHT.Knight(white), 'D', 6)
b_test.set_piece(KNIGHT.Knight(white), 'F', 6)
b_test.set_piece(KNIGHT.Knight(white), 'D', 4)
b_test.set_piece(KNIGHT.Knight(white), 'F', 4)
b_test.set_piece(KNIGHT.Knight(black), 'C', 6)
b_test.set_piece(KNIGHT.Knight(black), 'D', 7)
b_test.set_piece(KNIGHT.Knight(black), 'F', 7)
b_test.set_piece(KNIGHT.Knight(black), 'G', 6)
b_test.set_piece(KNIGHT.Knight(white), 'C', 4)


# Test
true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'E', 5, 'C', 6))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 6, 'E', 5))  # Move 2
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'D', 7))  # Move 3
true_values.append(True)
test_values.append(b_test.move_piece(white, 'D', 7, 'E', 5))  # Move 4
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'F', 7))  # Move 5
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 7, 'E', 5))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'G', 6))  # Move 7
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 6, 'E', 5))  # Move 8
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'G', 4))  # Move 9
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 4, 'E', 5))  # Move 10
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'F', 3))  # Move 11
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 3, 'E', 5))  # Move 12
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'D', 3))  # Move 13
true_values.append(True)
test_values.append(b_test.move_piece(white, 'D', 3, 'E', 5))  # Move 14
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'C', 4))  # Move 15
true_values.append(False)
test_values.append(b_test.move_piece(black, 'A', 8, 'C', 8))  # Move 16
true_values.append(False)
test_values.append(b_test.move_piece(black, 'A', 8, 'E', 5))  # Move 17
true_values.append(False)
test_values.append(b_test.move_piece(black, 'A', 8, 'B', 6))  # Move 18
true_values.append(True)
test_values.append(b_test.move_piece(black, 'H', 1, 'F', 3))  # Move 19
true_values.append(False)
test_values.append(b_test.move_piece(black, 'H', 1, 'G', 5))  # Move 20
true_values.append(False)
test_values.append(b_test.move_piece(black, 'H', 1, 'G', 3))  # Move 21
true_values.append(True)

print('-------------------- TRUE ---------------------\n')
b_true.print_board()
print('-------------------- TEST ---------------------\n')
b_test.print_board()


accurate = True
for i in range(len(true_values)):
    if true_values[i] != test_values[i]:
        accurate = False
        print('Error Move', i+1, '--- truth:', true_values[i], '||| test:', test_values[i])
