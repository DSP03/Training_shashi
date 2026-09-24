"""
Master Class 6 — Visualization
Topic: Line & Bar Charts (Matplotlib / Seaborn)

Run me directly:  python 09_viz_line_bar.py

This saves PNG files into the current folder AND calls plt.show() so it
works whether you're running it in a plain script or a notebook. If you're
running headless (no display), the show() call is a no-op — the PNGs are
still written.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")   # nicer default look, one line

# ---------------------------------------------------------------------
# Sample data: monthly revenue by product line
# ---------------------------------------------------------------------
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "widgets": [1000, 1100, 1050, 1300, 1250, 1400],
    "gadgets": [700, 750, 800, 780, 900, 950],
})

# ---------------------------------------------------------------------
# PART A — Line chart: great for trends over time
# ---------------------------------------------------------------------
plt.figure(figsize=(7, 4))
plt.plot(df["month"], df["widgets"], marker="o", label="Widgets")
plt.plot(df["month"], df["gadgets"], marker="o", label="Gadgets")
plt.title("Monthly Revenue by Product Line")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart_revenue.png", dpi=120)
print("Saved line_chart_revenue.png")
plt.show()
plt.close()


# ---------------------------------------------------------------------
# PART B — Bar chart: great for comparing categories
# ---------------------------------------------------------------------
totals = pd.DataFrame({
    "product": ["Widgets", "Gadgets"],
    "total_revenue": [df["widgets"].sum(), df["gadgets"].sum()],
})

plt.figure(figsize=(6, 4))
sns.barplot(data=totals, x="product", y="total_revenue")
plt.title("Total Revenue by Product (H1)")
plt.xlabel("")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("bar_chart_totals.png", dpi=120)
print("Saved bar_chart_totals.png")
plt.show()
plt.close()


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Show the same DataFrame producing two very different charts —")
    print("the choice of chart type communicates a different question:")
    print("'how does it change over time?' (line) vs. 'how do categories")
    print("compare?' (bar). Point out sns.set_theme() as a one-line upgrade")
    print("over raw matplotlib styling.")
