"""
Master Class 6 — NumPy & Pandas
Topic: Identifying & Handling Missing Data

Run me directly:  python 08_pandas_missing_data.py
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "age": [25, np.nan, 35, 28, np.nan],
    "salary": [95000, 72000, np.nan, 68000, 88000],
    "department": ["Engineering", "Sales", "Engineering", None, "Engineering"],
})
print("DataFrame with missing values:\n", df)


# ---------------------------------------------------------------------
# PART A — Detecting missing data
# ---------------------------------------------------------------------
print("\ndf.isna():\n", df.isna())
print("\nMissing values per column:\n", df.isna().sum())
print("\nAny missing values at all?", df.isna().values.any())
print("Rows with at least one missing value:\n", df[df.isna().any(axis=1)])


# ---------------------------------------------------------------------
# PART B — Dropping missing data
# ---------------------------------------------------------------------
dropped_rows = df.dropna()
print("\ndf.dropna() — drops ANY row with a missing value:\n", dropped_rows)

dropped_subset = df.dropna(subset=["age"])
print("\ndf.dropna(subset=['age']) — only drops rows missing 'age':\n", dropped_subset)


# ---------------------------------------------------------------------
# PART C — Filling missing data
# ---------------------------------------------------------------------
filled_mean = df.copy()
filled_mean["age"] = filled_mean["age"].fillna(filled_mean["age"].mean())
filled_mean["salary"] = filled_mean["salary"].fillna(filled_mean["salary"].mean())
print("\nNumeric columns filled with their column mean:\n", filled_mean)

filled_forward = df.copy()
filled_forward["department"] = filled_forward["department"].ffill()
print("\n'department' forward-filled (carries the previous valid value down):\n", filled_forward)

filled_constant = df.fillna({"department": "Unknown"})
print("\nFilling 'department' with a constant 'Unknown':\n", filled_constant)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Emphasize this is a JUDGMENT CALL, not a mechanical step: dropna()")
    print("throws away data, fillna(mean) can distort statistics, ffill() only")
    print("makes sense when order is meaningful. Ask trainees which they'd pick")
    print("for a 'department' column vs. a 'salary' column and why.")
