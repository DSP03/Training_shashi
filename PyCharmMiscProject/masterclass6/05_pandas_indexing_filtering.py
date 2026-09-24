"""
Master Class 6 — NumPy & Pandas
Topic: Indexing & Filtering DataFrames

Run me directly:  python 05_pandas_indexing_filtering.py
"""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "department": ["Engineering", "Sales", "Engineering", "Marketing", "Engineering"],
    "salary": [95000, 72000, 105000, 68000, 88000],
    "years_experience": [4, 8, 12, 2, 6],
})
print("Full DataFrame:\n", df)


# ---------------------------------------------------------------------
# PART A — loc (label-based) vs iloc (position-based)
# ---------------------------------------------------------------------
print("\ndf.loc[0]  (row labeled 0):\n", df.loc[0])
print("\ndf.loc[0, 'salary']:", df.loc[0, "salary"])
print("\ndf.iloc[0]  (first row by position):\n", df.iloc[0])
print("\ndf.iloc[0:2]  (first two rows):\n", df.iloc[0:2])


# ---------------------------------------------------------------------
# PART B — Boolean filtering — the pandas equivalent of a SQL WHERE clause
# ---------------------------------------------------------------------
engineers = df[df["department"] == "Engineering"]
print("\nEngineers only:\n", engineers)

high_earners = df[df["salary"] > 80000]
print("\nSalary > 80000:\n", high_earners)

# Combining conditions: & (and), | (or) — note the parentheses are required!
senior_engineers = df[(df["department"] == "Engineering") & (df["years_experience"] > 5)]
print("\nSenior engineers (Engineering AND 5+ years):\n", senior_engineers)


# ---------------------------------------------------------------------
# PART C — .query() — a more readable alternative for complex filters
# ---------------------------------------------------------------------
result = df.query("salary > 80000 and years_experience < 10")
print("\nUsing .query():\n", result)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("The classic Java-dev trap: writing 'df[df.department == \"Engineering\"")
    print("and df.salary > 80000]' with Python's 'and' instead of '&' — Python's")
    print("boolean operators don't work element-wise on Series, only & | ~ do.")
    print("Try it live and show the resulting ValueError.")
