# Imports
import sys
sys.path.append('../Pieces')
import pawn as PAWN
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
b_true.set_piece(PAWN.Pawn(black), 'C', 7)
b_true.set_piece(PAWN.Pawn(black), 'F', 7)
b_true.set_piece(PAWN.Pawn(black), 'H', 7)
b_true.set_piece(PAWN.Pawn(white), 'D', 6)
b_true.set_piece(PAWN.Pawn(white), 'G', 6)
b_true.set_piece(PAWN.Pawn(black), 'A', 5)
b_true.set_piece(PAWN.Pawn(white), 'H', 4)
b_true.set_piece(PAWN.Pawn(black), 'A', 3)
b_true.set_piece(PAWN.Pawn(white), 'F', 3)
b_true.set_piece(QUEEN.Queen(black), 'B', 1)

#   Test Board
b_test.has_king = False
b_test.set_piece(PAWN.Pawn(white), 'A', 2)
b_test.set_piece(PAWN.Pawn(white), 'B', 2)
b_test.set_piece(PAWN.Pawn(white), 'C', 2)
b_test.set_piece(PAWN.Pawn(white), 'D', 2)
b_test.set_piece(PAWN.Pawn(white), 'E', 2)
b_test.set_piece(PAWN.Pawn(white), 'F', 2)
b_test.set_piece(PAWN.Pawn(white), 'G', 2)
b_test.set_piece(PAWN.Pawn(white), 'H', 2)
b_test.set_piece(PAWN.Pawn(black), 'A', 7)
b_test.set_piece(PAWN.Pawn(black), 'B', 7)
b_test.set_piece(PAWN.Pawn(black), 'C', 7)
b_test.set_piece(PAWN.Pawn(black), 'D', 7)
b_test.set_piece(PAWN.Pawn(black), 'E', 7)
b_test.set_piece(PAWN.Pawn(black), 'F', 7)
b_test.set_piece(PAWN.Pawn(black), 'G', 7)
b_test.set_piece(PAWN.Pawn(black), 'H', 7)
b_test.set_piece(PAWN.Pawn(black), 'F', 4)
b_test.set_piece(PAWN.Pawn(black), 'F', 3)
b_test.set_piece(PAWN.Pawn(black), 'G', 3)


# Test
true_values = []
test_values = []

test_values.append(b_test.move_piece(white, 'E', 2, 'E', 4))  # Move 1
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 7, 'E', 5))  # Move 2
true_values.append(False)
test_values.append(b_test.move_piece(black, 'E', 7, 'E', 5))  # Move 3
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 4, 'E', 5))  # Move 4
true_values.append(False)
test_values.append(b_test.move_piece(black, 'D', 2, 'D', 4))  # Move 5
true_values.append(False)
test_values.append(b_test.move_piece(white, 'D', 2, 'D', 4))  # Move 6
true_values.append(True)
test_values.append(b_test.move_piece(black, 'E', 5, 'D', 4))  # Move 7
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 2, 'C', 3))  # Move 8
true_values.append(True)
test_values.append(b_test.move_piece(black, 'D', 4, 'C', 3))  # Move 9
true_values.append(True)
test_values.append(b_test.move_piece(white, 'H', 2, 'H', 4))  # Move 10
true_values.append(True)
test_values.append(b_test.move_piece(black, 'C', 3, 'B', 2))  # Move 11
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 2, 'F', 3))  # Move 12
true_values.append(False)
test_values.append(b_test.move_piece(white, 'F', 2, 'F', 4))  # Move 13
true_values.append(False)
test_values.append(b_test.move_piece(white, 'G', 2, 'G', 4))  # Move 14
true_values.append(False)
test_values.append(b_test.move_piece(white, 'G', 2, 'F', 3))  # Move 15
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 3, 'E', 4))  # Move 16
true_values.append(False)
test_values.append(b_test.move_piece(white, 'E', 4, 'D', 5))  # Move 17
true_values.append(False)
test_values.append(b_test.move_piece(white, 'E', 4, 'E', 6))  # Move 18
true_values.append(False)
test_values.append(b_test.move_piece(black, 'A', 7, 'A', 8))  # Move 19
true_values.append(False)
test_values.append(b_test.move_piece(black, 'A', 7, 'A', 5))  # Move 20
true_values.append(True)
test_values.append(b_test.move_piece(white, 'C', 5, 'A', 8))  # Move 21
true_values.append(False)
test_values.append(b_test.move_piece(white, 'F', 2, 'G', 3))  # Move 22
true_values.append(True)
test_values.append(b_test.move_piece(white, 'G', 3, 'F', 4))  # Move 23
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 4, 'F', 6))  # Move 24
true_values.append(False)

# En Passant Test for White
test_values.append(b_test.move_piece(white, 'E', 4, 'E', 5))  # Move 25
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 4, 'F', 5))  # Move 26
true_values.append(True)
test_values.append(b_test.move_piece(black, 'D', 7, 'D', 5))  # Move 27
true_values.append(True)
test_values.append(b_test.move_piece(white, 'E', 5, 'D', 6))  # Move 28 En Passant
true_values.append(True)
test_values.append(b_test.move_piece(black, 'G', 7, 'G', 5))  # Move 29
true_values.append(True)
test_values.append(b_test.move_piece(white, 'F', 5, 'G', 6))  # Move 30 En Passant
true_values.append(True)
test_values.append(b_test.move_piece(black, 'B', 7, 'B', 5))  # Move 31
true_values.append(True)
test_values.append(b_test.move_piece(black, 'B', 5, 'B', 4))  # Move 32
true_values.append(True)
test_values.append(b_test.move_piece(white, 'A', 2, 'A', 4))  # Move 33
true_values.append(True)
test_values.append(b_test.move_piece(black, 'B', 4, 'A', 3))  # Move 34
true_values.append(True)
test_values.append(b_test.move_piece(black, 'B', 2, 'B', 1))  # Move 35
true_values.append(True)
test_values.append(b_test.move_piece(black, 'D', 5, 'D', 4))  # Move 36 En Passant Piece Removal
true_values.append(False)
test_values.append(b_test.move_piece(black, 'B', 1, 'H', 1))  # Move 37 Queening Piece
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
