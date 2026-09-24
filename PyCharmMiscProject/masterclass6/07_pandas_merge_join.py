"""
Master Class 6 — NumPy & Pandas
Topic: Merging & Joining DataFrames

Run me directly:  python 07_pandas_merge_join.py
"""

import pandas as pd

employees = pd.DataFrame({
    "employee_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Carol", "Dave"],
    "department_id": [10, 20, 10, 30],
})

departments = pd.DataFrame({
    "department_id": [10, 20, 30],
    "department_name": ["Engineering", "Sales", "Marketing"],
})

print("employees:\n", employees)
print("\ndepartments:\n", departments)


# ---------------------------------------------------------------------
# PART A — Inner join (like SQL INNER JOIN) — the default
# ---------------------------------------------------------------------
merged_inner = pd.merge(employees, departments, on="department_id", how="inner")
print("\nInner join on department_id:\n", merged_inner)


# ---------------------------------------------------------------------
# PART B — Left join — keep every row from the left table
# ---------------------------------------------------------------------
# Add an employee whose department_id doesn't exist in `departments`
employees_with_orphan = pd.concat([
    employees,
    pd.DataFrame({"employee_id": [5], "name": ["Eve"], "department_id": [99]}),
], ignore_index=True)

merged_left = pd.merge(employees_with_orphan, departments, on="department_id", how="left")
print("\nLeft join (Eve's department_id=99 doesn't exist in departments):\n", merged_left)
print("\nNote Eve's department_name is NaN — left join keeps her row anyway.")


# ---------------------------------------------------------------------
# PART C — Concatenating DataFrames (stacking rows)
# ---------------------------------------------------------------------
q1_sales = pd.DataFrame({"month": ["Jan", "Feb", "Mar"], "revenue": [1000, 1100, 1200]})
q2_sales = pd.DataFrame({"month": ["Apr", "May", "Jun"], "revenue": [1300, 1250, 1400]})

first_half = pd.concat([q1_sales, q2_sales], ignore_index=True)
print("\nConcatenated Q1 + Q2 sales:\n", first_half)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Draw the parallel to SQL explicitly: pd.merge(..., how='inner') is")
    print("INNER JOIN, how='left' is LEFT JOIN. pd.concat() is closer to UNION —")
    print("stacking rows rather than matching on a key.")
