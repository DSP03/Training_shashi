"""
Master Class 6 — NumPy & Pandas
Topic: NumPy Arrays vs. Python Lists & Vectorized Operations

Run me directly:  python 01_numpy_arrays_vs_lists.py
"""

import numpy as np
import time

# ---------------------------------------------------------------------
# PART A — Why arrays instead of lists?
# ---------------------------------------------------------------------
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print("Python list:", python_list)
print("NumPy array:", numpy_array)
print("Array dtype:", numpy_array.dtype)
print("Array shape:", numpy_array.shape)

# --- Element-wise math: lists need a loop, arrays just work ---
doubled_list = [x * 2 for x in python_list]     # list comprehension required
doubled_array = numpy_array * 2                  # vectorized — no loop needed

print("\nDoubled list (loop):", doubled_list)
print("Doubled array (vectorized):", doubled_array)

try:
    python_list * 2 == [2, 4, 6, 8, 10]  # this actually just repeats the list!
    print("\n[1,2,3] * 2 in plain Python repeats the list:", python_list * 2)
except Exception as e:
    print(e)


# ---------------------------------------------------------------------
# PART B — Performance: vectorized beats loops at scale
# ---------------------------------------------------------------------
N = 2_000_000
big_list = list(range(N))
big_array = np.arange(N)

start = time.perf_counter()
result_list = [x * 2 for x in big_list]
list_time = time.perf_counter() - start

start = time.perf_counter()
result_array = big_array * 2
array_time = time.perf_counter() - start

print(f"\nDoubling {N:,} elements:")
print(f"  Python loop:      {list_time:.4f}s")
print(f"  NumPy vectorized: {array_time:.4f}s")
print(f"  NumPy was ~{list_time / array_time:.0f}x faster")


# ---------------------------------------------------------------------
# PART C — 2D arrays (matrices) and basic operations
# ---------------------------------------------------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", matrix)
print("Shape:", matrix.shape, "| Sum:", matrix.sum(), "| Mean:", matrix.mean())
print("Column sums (axis=0):", matrix.sum(axis=0))
print("Row sums (axis=1):", matrix.sum(axis=1))


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Run this file and let the timing numbers speak for themselves —")
    print("vectorized NumPy operations are the foundation of every ML")
    print("framework's performance (PyTorch tensors work the same way).")
