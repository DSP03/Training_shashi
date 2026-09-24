"""
Master Class 6 — NumPy & Pandas
Topic: Series & DataFrame Basics

Run me directly:  python 03_pandas_series_dataframe.py
"""

import pandas as pd

# ---------------------------------------------------------------------
# PART A — Series: a single labeled column of data
# ---------------------------------------------------------------------
scores = pd.Series([88, 92, 79, 95], index=["Alice", "Bob", "Carol", "Dave"])
print("Series:\n", scores)
print("\nscores['Bob']:", scores["Bob"])
print("scores.mean():", scores.mean())
print("scores[scores > 85]:\n", scores[scores > 85])


# ---------------------------------------------------------------------
# PART B — DataFrame: a table, like a whole spreadsheet
# ---------------------------------------------------------------------
data = {
    "name": ["Alice", "Bob", "Carol", "Dave"],
    "age": [25, 30, 35, 28],
    "department": ["Engineering", "Sales", "Engineering", "Marketing"],
    "salary": [95000, 72000, 105000, 68000],
}
df = pd.DataFrame(data)

print("\nDataFrame:\n", df)
print("\ndf.shape:", df.shape)
print("df.columns:", list(df.columns))
print("df.dtypes:\n", df.dtypes)

print("\ndf.head(2):\n", df.head(2))
print("\ndf.describe():\n", df.describe())

# --- Selecting a column returns a Series ---
print("\ndf['name'] (a Series):\n", df["name"])
print("\ntype(df['name']):", type(df["name"]))

# --- Selecting multiple columns returns a DataFrame ---
print("\ndf[['name', 'salary']]:\n", df[["name", "salary"]])


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Point out: a DataFrame is basically a dict of Series sharing one")
    print("index. Selecting one column (df['name']) gives a Series; selecting")
    print("several columns (df[['name','salary']]) gives back a DataFrame.")
