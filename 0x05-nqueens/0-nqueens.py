#!/usr/bin/python3
"""The N-queens challenge"""
import sys


def board_init(n):
    """Initializes chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """deepcopy"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """return the solution"""
    solution = []
    for rw in range(len(board)):
        for cl in range(len(board)):
            if board[rw][cl] == "Q":
                solution.append([rw, cl])
                break
    return (solution)


def xout(board, row, col):
    """chessboard X out spots"""
    # X out all forward spots
    for cl in range(col + 1, len(board)):
        board[row][cl] = "x"
    # X out all backwards spots
    for cl in range(col - 1, -1, -1):
        board[row][cl] = "x"
    # X out all spots below
    for rw in range(row + 1, len(board)):
        board[rw][col] = "x"
    # X out all spots above
    for rw in range(row - 1, -1, -1):
        board[rw][col] = "x"
    # X out all spots diagonally down to the right
    cl = col + 1
    for rw in range(row + 1, len(board)):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1
    # X out all spots diagonally up to the left
    cl = col - 1
    for rw in range(row - 1, -1, -1):
        if cl < 0:
            break
        board[rw][cl]
        cl -= 1
    # X out all spots diagonally up to the right
    cl = col + 1
    for rw in range(row - 1, -1, -1):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1
    # X out all spots diagonally down to the left
    cl = col - 1
    for rw in range(row + 1, len(board)):
        if cl < 0:
            break
        board[rw][cl] = "x"
        cl -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursive solve"""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for cl in range(len(board)):
        if board[row][cl] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][cl] = "Q"
            xout(tmp_board, row, cl)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = board_init(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
