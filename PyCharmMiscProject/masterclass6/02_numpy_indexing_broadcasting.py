"""
Master Class 6 — NumPy & Pandas
Topic: NumPy Indexing, Slicing & Broadcasting

Run me directly:  python 02_numpy_indexing_broadcasting.py
"""

import numpy as np

# ---------------------------------------------------------------------
# PART A — Indexing & slicing (similar to lists, but more powerful)
# ---------------------------------------------------------------------
arr = np.array([10, 20, 30, 40, 50])

print("arr:", arr)
print("arr[0]:", arr[0])
print("arr[-1]:", arr[-1])
print("arr[1:3]:", arr[1:3])
print("arr[::2] (every other):", arr[::2])

# --- Boolean indexing / masking — very common in data cleaning ---
mask = arr > 25
print("\nMask (arr > 25):", mask)
print("arr[mask]:", arr[mask])
print("Shortcut, same thing:", arr[arr > 25])


# ---------------------------------------------------------------------
# PART B — 2D indexing
# ---------------------------------------------------------------------
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("\ngrid:\n", grid)
print("grid[1, 2] (row 1, col 2):", grid[1, 2])
print("grid[:, 0] (first column):", grid[:, 0])
print("grid[1, :] (second row):", grid[1, :])


# ---------------------------------------------------------------------
# PART C — Broadcasting: operating on arrays of different shapes
# ---------------------------------------------------------------------
prices = np.array([100, 200, 300])
tax_rate = 1.08   # a single scalar "broadcasts" across every element

print("\nprices:", prices)
print("prices * tax_rate (broadcasting a scalar):", prices * tax_rate)

# Broadcasting a smaller array across a bigger one
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_adjustment = np.array([10, 20, 30])   # shape (3,) broadcasts across each row

print("\nmatrix:\n", matrix)
print("matrix + row_adjustment:\n", matrix + row_adjustment)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Show arr[arr > 25] first — it's the single most-used NumPy pattern")
    print("in real data cleaning. Then show broadcasting: no loop was needed")
    print("to apply tax_rate to every price, or row_adjustment to every row.")
