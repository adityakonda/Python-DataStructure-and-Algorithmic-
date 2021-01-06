board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

def findLegalMoves(board, starting_position):
  x = [1, 0, -1, 0]
  y = [0, -1, 0, 1]

  # get the height of the board
  nY = len(board)

  # if the height of the board is zero, the width will be zero too, otherwise, get the width of the board by getting the length of the first row
  nX = 0 if nY == 0 else len(board[0])

  # store possible moves into this list
  possiblePosition = []

  # loop through all possible neighbor in the following: right, down, left, up
  for idx, xx in enumerate(x):
    newX = starting_position[1] + xx
    newY = starting_position[0] + y[idx]
    # if this cell is not in the board, skip it
    if not (0 <= newX < nX and 0 <= newY < nY):
      continue
    # if this cell is wall, skip it
    if board[newY][newX] == -1:
      continue

    possiblePosition.append([newY, newX])

  print(possiblePosition)

if __name__ == '__main__':
    findLegalMoves(board, (5, 3))