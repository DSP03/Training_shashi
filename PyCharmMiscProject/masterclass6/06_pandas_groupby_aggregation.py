"""
Master Class 6 — NumPy & Pandas
Topic: GroupBy & Aggregation

Run me directly:  python 06_pandas_groupby_aggregation.py
"""

import pandas as pd

df = pd.DataFrame({
    "department": ["Engineering", "Sales", "Engineering", "Marketing", "Engineering", "Sales"],
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"],
    "salary": [95000, 72000, 105000, 68000, 88000, 76000],
    "years_experience": [4, 8, 12, 2, 6, 3],
})
print("Full DataFrame:\n", df)


# ---------------------------------------------------------------------
# PART A — Basic groupby + a single aggregation
# ---------------------------------------------------------------------
avg_salary_by_dept = df.groupby("department")["salary"].mean()
print("\nAverage salary by department:\n", avg_salary_by_dept)

headcount_by_dept = df.groupby("department").size()
print("\nHeadcount by department:\n", headcount_by_dept)


# ---------------------------------------------------------------------
# PART B — Multiple aggregations at once with .agg()
# ---------------------------------------------------------------------
summary = df.groupby("department")["salary"].agg(["mean", "min", "max", "count"])
print("\nMulti-stat summary by department:\n", summary)

# Aggregate different columns differently
multi_col_summary = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    total_experience=("years_experience", "sum"),
    headcount=("name", "count"),
)
print("\nNamed, multi-column aggregation:\n", multi_col_summary)


# ---------------------------------------------------------------------
# PART C — Sorting the result
# ---------------------------------------------------------------------
sorted_summary = multi_col_summary.sort_values("avg_salary", ascending=False)
print("\nSorted by avg_salary (descending):\n", sorted_summary)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("groupby().agg(name=('col', 'func')) is the pattern worth memorizing —")
    print("it reads almost like a SQL 'GROUP BY ... SELECT AVG(salary) AS avg_salary'.")
    print("Compare this line-by-line to an equivalent SQL query on the whiteboard.")
