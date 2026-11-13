# Assignment 2: N-Queens Problem using Backtracking

n = int(input("Enter n (size of board): "))

r0 = int(input("Row of first queen (1 to n): ")) - 1
c0 = int(input("Column of first queen (1 to n): ")) - 1

if not (0 <= r0 < n and 0 <= c0 < n):
    raise SystemExit("Position is outside the board")

board = [-1] * n
# board[row] = column of the queen in that row, -1 = empty

board[r0] = c0

backtracks = 0


def safe(row, col):
    for r in range(n):
        c = board[r]

        if r != row and c != -1 and (
            c == col or abs(c - col) == abs(r - row)
        ):
            return False

    return True


def solve(row):
    global backtracks

    if row == n:
        return True

    if board[row] != -1:
        # Row of the pre-placed queen
        return solve(row + 1)

    for col in range(n):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1
            # Dead end: remove queen (backtrack)

            backtracks += 1

    return False


if solve(0):
    print("\nFinal %dx%d matrix (1 = queen):" % (n, n))

    for r in range(n):
        print(" ".join(
            "1" if board[r] == c else "0"
            for c in range(n)
        ))

    print("Queen positions (row, col):",
          [(r + 1, board[r] + 1) for r in range(n)])

else:
    print("\nNo solution with the first queen at (%d, %d)"
          % (r0 + 1, c0 + 1))

print("Backtracks =", backtracks)