def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    if col >= len(board):
        return 1

    count = 0
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            count += solve_nq_util(board, col + 1)
            board[i][col] = 0

    return count

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return solve_nq_util(board, 0)

n = 8
result = solve_n_queens(n)
print(f"Число уникальных расстановок {n} ферзей на доске {n}x{n}: {result}")
