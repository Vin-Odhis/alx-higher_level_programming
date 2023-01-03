#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

import sys

def is_safe(board, row, col, N):
    # check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check if there is a queen in the top-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check if there is a queen in the top-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row, N):
    if row == N:
        # if all queens are placed, print the solution
        print_solution(board, N)
        return True
    else:
        # try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                # place the queen and move to the next row
                board[row][col] = 1
                if solve(board, row+1, N):
                    return True
                # backtrack and remove the queen from the current position
                board[row][col] = 0
        return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0] * N for _ in range(N)]
    solve(board, 0, N)

if __name__ == "__main__":
    main()
