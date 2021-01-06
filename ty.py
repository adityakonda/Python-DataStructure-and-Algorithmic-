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
  return possiblePosition

"""
We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can be a wall (denoted by -1) or a blank space (0).

board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall, or go through the edges of the board.

Write a function that, given a board and a player starting position (represented as a row-column pair), returns all of the possible next positions for the player.

Sample inputs (board, starting_position) and outputs (in any order):

findLegalMoves(board, (1, 1)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (5, 3)) =>
  (5, 2), (5, 4), (4, 3), (6, 3)

findLegalMoves(board, (5, 1)) =>
  (6, 1), (4, 1), (5, 0), (5, 2)

findLegalMoves(board, (6, 0)) =>
  (5, 0), (6, 1)

findLegalMoves(board, (6, 4)) =>
  (5, 4), (6, 3)

findLegalMoves(board, (0, 0)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (2, 2)) =>
  [empty]

n: width of the input board
m: height of the input board

"""

board = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

start1 = (1, 1)
start2 = (5, 3)
start3 = (5, 1)
start4 = (6, 0)
start5 = (6, 4)
start6 = (0, 0)
start7 = (2, 2)


def validate(board, x, y):
    zeros = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                zeros.append([i, j])

    print(zeros)

    for i in zeros:
        x = i[0]
        y = i[1]


if __name__ == '__main__':
    print(validate(board))