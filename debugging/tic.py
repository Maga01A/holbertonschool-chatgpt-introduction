#!/usr/bin/env python3
import sys

def print_board(board):
    """Print the tic-tac-toe board in a readable format."""
    for r, row in enumerate(board):
        print(" " + " | ".join(row))
        if r < len(board) - 1:
            print("---+---+---")

def check_winner(board):
    """Return True if there is a winner on the board, otherwise False."""
    size = len(board)
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == size:
            return True
    # Check columns
    for col in range(size):
        col_vals = [board[row][col] for row in range(size)]
        if col_vals[0] != " " and col_vals.count(col_vals[0]) == size:
            return True
    # Check diagonals
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(size)):
        return True
    if board[0][size-1] != " " and all(board[i][size-1-i] == board[0][size-1] for i in range(size)):
        return True
    return False

def board_full(board):
    """Return True if the board has no empty cells."""
    return all(cell != " " for row in board for cell in row)

def get_coordinate(prompt):
    """
    Prompt the user and validate the coordinate input.
    Tests all user inputs: non-numeric, out-of-range, empty, and handles EOF/KeyboardInterrupt.
    Returns an int 0..2, or raises SystemExit if the user requests quit/interrupts.
    """
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput canceled. Exiting game.")
            raise SystemExit(0)

        if raw.lower() in ("q", "quit", "exit"):
            print("Quit command received. Exiting game.")
            raise SystemExit(0)
        if raw == "":
            print("Empty input. Please enter 0, 1, or 2 (or 'q' to quit).")
            continue
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue
        if val < 0 or val > 2:
            print("Out of range. Enter 0, 1, or 2.")
            continue
        return val

def tic_tac_toe():
    """Play a two-player (X and O) tic-tac-toe game in the terminal."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn. (Enter 'q' to quit)")
        # Get a valid row and column (all inputs tested)
        try:
            row = get_coordinate("Enter row (0, 1, or 2): ")
            col = get_coordinate("Enter column (0, 1, or 2): ")
        except SystemExit:
            return

        # Check if spot is available
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player

        # Check for a win immediately after the move
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except SystemExit:
        # graceful exit already handled in get_coordinate
        pass#!/usr/bin/env python3
import sys

def print_board(board):
    """Print the tic-tac-toe board in a readable format."""
    for r, row in enumerate(board):
        print(" " + " | ".join(row))
        if r < len(board) - 1:
            print("---+---+---")

def check_winner(board):
    """Return True if there is a winner on the board, otherwise False."""
    size = len(board)
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == size:
            return True
    # Check columns
    for col in range(size):
        col_vals = [board[row][col] for row in range(size)]
        if col_vals[0] != " " and col_vals.count(col_vals[0]) == size:
            return True
    # Check diagonals
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(size)):
        return True
    if board[0][size-1] != " " and all(board[i][size-1-i] == board[0][size-1] for i in range(size)):
        return True
    return False

def board_full(board):
    """Return True if the board has no empty cells."""
    return all(cell != " " for row in board for cell in row)

def get_coordinate(prompt):
    """
    Prompt the user and validate the coordinate input.
    Tests all user inputs: non-numeric, out-of-range, empty, and handles EOF/KeyboardInterrupt.
    Returns an int 0..2, or raises SystemExit if the user requests quit/interrupts.
    """
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput canceled. Exiting game.")
            raise SystemExit(0)

        if raw.lower() in ("q", "quit", "exit"):
            print("Quit command received. Exiting game.")
            raise SystemExit(0)
        if raw == "":
            print("Empty input. Please enter 0, 1, or 2 (or 'q' to quit).")
            continue
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue
        if val < 0 or val > 2:
            print("Out of range. Enter 0, 1, or 2.")
            continue
        return val

def tic_tac_toe():
    """Play a two-player (X and O) tic-tac-toe game in the terminal."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn. (Enter 'q' to quit)")
        # Get a valid row and column (all inputs tested)
        try:
            row = get_coordinate("Enter row (0, 1, or 2): ")
            col = get_coordinate("Enter column (0, 1, or 2): ")
        except SystemExit:
            return

        # Check if spot is available
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player

        # Check for a win immediately after the move
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except SystemExit:
        # graceful exit already handled in get_coordinate
        pass
