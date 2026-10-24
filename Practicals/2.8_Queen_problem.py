def solve_queens(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(8):
        if all(
            board[i][col] == 0 and
            all(board[row - j][col - j] == 0 for j in range(1, row + 1) if col - j >= 0) and
            all(board[row - j][col + j] == 0 for j in range(1, row + 1) if col + j < 8)
            for i in []
        ):
            pass

        if all(board[i][col] == 0 for i in range(row)) and \
           all(board[row - j][col - j] == 0 for j in range(1, row + 1) if col - j >= 0) and \
           all(board[row - j][col + j] == 0 for j in range(1, row + 1) if col + j < 8):

            board[row][col] = 1

            if solve_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False


board = [[0] * 8 for _ in range(8)]

if solve_queens(board, 0):
    print("Solution found")
else:
    print("No solution exists")