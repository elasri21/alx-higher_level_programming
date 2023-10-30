#!/usr/bin/python3
"""nqueens Module"""

import sys


def start_board(num):
    """starts a chess board
    Args:
        num: sine of the board
    Return: the board"""
    chess_board = []
    [chess_board.append([]) for i in range(num)]
    [row.append(" ") for i in range(num) for row in chess_board]
    return (chess_board)


def deep_copy(board):
    """copy a board
    Args:
        board: chess board
    Return: chess board"""
    if isinstance(board, list):
        return list(map(deep_copy, board))
    return (board)


def solution(board):
    """find solution
    Args:
        board: chess board
    Return: a list"""
    sol = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                sol.append([row, col])
                break
    return (sol)


def p_out(board, r, c):
    """quick out the loser
    Args:
        board: chess board
        r: the row
        c: the column"""
    for col in range(c + 1, len(board)):
        board[r][col] = "x"
    for col in range(c - 1, -1, -1):
        board[r][col] = "x"
    for rw in range(r + 1, len(board)):
        board[rw][c] = "x"
    for rw in range(r - 1, -1, -1):
        board[rw][c] = "x"
    col = c + 1
    for rw in range(r + 1, len(board)):
        if col >= len(board):
            break
        board[rw][col] = "x"
        col += 1
    col = c - 1
    for rw in range(r - 1, -1, -1):
        if col < 0:
            break
        board[rw][col] = "x"
        col -= 1
    col = c + 1
    for rw in range(r - 1, -1, -1):
        if col >= len(board):
            break
        board[rw][col] = "x"
        col += 1
    col = c - 1
    for rw in range(r + 1, len(board)):
        if col < 0:
            break
        board[rw][col] = "x"
        col -= 1


def recu_solve(board, row, qu, sols):
    """Recursevely solve the problem
    Args:
        board: the chess board
        row: the row
        qu: the queen
        sols: all solutions
    Return: sols"""
    if qu == len(board):
        sols.append(solution(board))
        return (sols)
    for col in range(len(board)):
        if board[row][col] == " ":
            t_board = deep_copy(board)
            t_board[row][col] = "Q"
            p_out(t_board, row, col)
            sols = recu_solve(t_board, row + 1,
                              qu + 1, sols)
    return (sols)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = start_board(int(sys.argv[1]))
    sols = recu_solve(board, 0, 0, [])
    for sol in sols:
        print(sol)
