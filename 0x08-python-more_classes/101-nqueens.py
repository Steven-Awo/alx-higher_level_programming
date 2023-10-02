#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_board(n):
    """Initializing an `n`x`n` sized chessboard with 0's."""
    boardr = []
    [boardr.append([]) for a in range(n)]
    [roww.append(' ') for a in range(n) for roww in boardr]
    return (boardr)

def board_deepcopy(boardr):
    """Return a deepcopy of a chessboard."""
    if isinstance(boardr, list) is True:
        return list(map(board_deepcopy, boardr))
    return (boardr)

def get_solution(boardr):
    """Returning the list of the lists representations of a solved chessboard."""
    solutions = []
    for rw in range(len(boardr)):
        for coln in range(len(boardr)):
            if boardr[rw][coln] == "Q":
                solutions.append([rw, coln])
                break
    return (solutions)

def xout(boardr, roww, colln):
    """X out spots on a chessboard.

    All the spots where non-attacking queens can't
    be played are X-ed out.

    Args:
        boardr (list): The present working chessboard.
        roww (int): The roww to where the queen was last played.
        colln (int): The column to where the queen was last played.
    """
    # X out all forward spots
    for coln in range(colln + 1, len(boardr)):
        boardr[roww][coln] = "x"
    # X out all backwards spots
    for coln in range(colln - 1, -1, -1):
        boardr[roww][coln] = "x"
    # X out all spots below
    for rw in range(roww + 1, len(boardr)):
        boardr[rw][colln] = "x"
    # X out all spots above
    for rw in range(roww - 1, -1, -1):
        boardr[rw][colln] = "x"
    # X out all spots diagonally down to the right
    coln = colln + 1
    for rw in range(roww + 1, len(boardr)):
        if coln >= len(boardr):
            break
        boardr[rw][coln] = "x"
        coln += 1
    # X out all spots diagonally up to the left
    coln = colln - 1
    for rw in range(roww - 1, -1, -1):
        if coln < 0:
            break
        boardr[rw][coln]
        coln -= 1
    # X out all spots diagonally up to the right
    coln = colln + 1
    for rw in range(roww - 1, -1, -1):
        if coln >= len(boardr):
            break
        boardr[rw][coln] = "x"
        coln += 1
    # X out all spots diagonally down to the left
    coln = colln - 1
    for rw in range(roww + 1, len(boardr)):
        if coln < 0:
            break
        boardr[rw][coln] = "x"
        coln -= 1

def recursive_solve(boardr, roww, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        boardr (list): The present working chessboard.
        roww (int): The present working roww.
        queens (int): The present number of the placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(boardr):
        solutions.append(get_solution(boardr))
        return (solutions)

    for coln in range(len(boardr)):
        if boardr[roww][coln] == " ":
            temp_board = board_deepcopy(boardr)
            temp_board[roww][coln] = "Q"
            xout(temp_board, roww, coln)
            solutions = recursive_solve(temp_board, roww + 1,
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

    boardr = init_board(int(sys.argv[1]))
    solutions = recursive_solve(boardr, 0, 0, [])
    for solu in solutions:
        print(solu)
