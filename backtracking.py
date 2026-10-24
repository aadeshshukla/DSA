def solve_n_queens(n: int):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    # Sets to track columns and diagonals under attack in O(1) time
    cols = set()
    diag_pos = set()  # (row + col) remains constant
    diag_neg = set()  # (row - col) remains constant

    def backtrack(row: int):
        # Base case: successfully placed all N queens
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Check if this square is safe
            if col in cols or (row + col) in diag_pos or (row - col) in diag_neg:
                continue

            # 1. Make choice
            board[row][col] = "Q"
            cols.add(col)
            diag_pos.add(row + col)
            diag_neg.add(row - col)

            # 2. Explore next row
            backtrack(row + 1)

            # 3. Undo choice (Backtrack)
            board[row][col] = "."
            cols.remove(col)
            diag_pos.remove(row + col)
            diag_neg.remove(row - col)

    backtrack(0)
    return solutions


# Example usage: Solve for 4 queens
n = 4
results = solve_n_queens(n)

print(f"Total solutions for {n}-Queens: {len(results)}\n")
for idx, solution in enumerate(results, 1):
    print(f"Solution {idx}:")
    for row in solution:
        print(row)
    print()
