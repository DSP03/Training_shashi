"""
Master Class 6 — NumPy & Pandas
Topic: Reading CSV / Excel Files

Run me directly:  python 04_pandas_read_csv_excel.py

This script first WRITES a small sample dataset to disk (sample_sales.csv
and sample_sales.xlsx) so it's fully self-contained — no external file
needed to follow along.
"""

import pandas as pd

# ---------------------------------------------------------------------
# Step 0 — Create a sample dataset to read back (so this file is standalone)
# ---------------------------------------------------------------------
sample = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "product": ["Widget", "Gadget", "Widget", "Gizmo", "Gadget"],
    "region": ["East", "West", "East", "North", "West"],
    "units": [10, 5, 8, 12, 7],
    "unit_price": [9.99, 19.99, 9.99, 14.99, 19.99],
})
sample.to_csv("sample_sales.csv", index=False)
sample.to_excel("sample_sales.xlsx", index=False, sheet_name="Sales")
print("Wrote sample_sales.csv and sample_sales.xlsx\n")


# ---------------------------------------------------------------------
# PART A — Reading CSV
# ---------------------------------------------------------------------
df_csv = pd.read_csv("sample_sales.csv")
print("Read from CSV:\n", df_csv)
print("\ndf_csv.info():")
df_csv.info()


# ---------------------------------------------------------------------
# PART B — Reading Excel
# ---------------------------------------------------------------------
df_excel = pd.read_excel("sample_sales.xlsx", sheet_name="Sales")
print("\nRead from Excel:\n", df_excel)


# ---------------------------------------------------------------------
# PART C — A couple of handy read_csv options
# ---------------------------------------------------------------------
df_subset = pd.read_csv(
    "sample_sales.csv",
    usecols=["product", "region", "units"],   # only load the columns you need
)
print("\nOnly selected columns:\n", df_subset)

df_indexed = pd.read_csv("sample_sales.csv", index_col="order_id")
print("\nUsing order_id as the index:\n", df_indexed)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Point out that read_csv and read_excel return the exact same kind")
    print("of DataFrame regardless of source format — everything downstream")
    print("(filtering, grouping, plotting) works identically either way.")
