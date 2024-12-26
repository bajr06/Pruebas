board = []
EMPTY = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

ROOK = board[0][0]
ROOK = board[0][7]
ROOK = board[7][0]
ROOK = board[7][7]

KNIGHT = board[4][4]

PAWN = board[3][4]

print(board)
print(ROOK)
print(KNIGHT)
print(PAWN)
