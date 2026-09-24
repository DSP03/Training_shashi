"""
Master Class 6 — Visualization
Topic: Scatter & Histogram Charts (Matplotlib / Seaborn)

Run me directly:  python 10_viz_scatter_histogram.py
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
rng = np.random.default_rng(42)   # fixed seed so the demo is reproducible

# ---------------------------------------------------------------------
# Sample data: years of experience vs. salary, across departments
# ---------------------------------------------------------------------
n = 60
df = pd.DataFrame({
    "years_experience": rng.uniform(0, 15, n),
    "department": rng.choice(["Engineering", "Sales", "Marketing"], n),
})
# salary roughly correlated with experience, plus noise, plus a department bump
dept_bump = df["department"].map({"Engineering": 15000, "Sales": 5000, "Marketing": 0})
df["salary"] = 55000 + df["years_experience"] * 4000 + dept_bump + rng.normal(0, 5000, n)


# ---------------------------------------------------------------------
# PART A — Scatter plot: great for relationships between two numeric variables
# ---------------------------------------------------------------------
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="years_experience", y="salary", hue="department")
plt.title("Salary vs. Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.savefig("scatter_salary_experience.png", dpi=120)
print("Saved scatter_salary_experience.png")
plt.show()
plt.close()


# ---------------------------------------------------------------------
# PART B — Histogram: great for seeing the SHAPE/distribution of one variable
# ---------------------------------------------------------------------
plt.figure(figsize=(7, 5))
sns.histplot(data=df, x="salary", bins=15, kde=True)
plt.title("Distribution of Salaries")
plt.xlabel("Salary ($)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram_salary.png", dpi=120)
print("Saved histogram_salary.png")
plt.show()
plt.close()


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Scatter answers 'is there a relationship between X and Y?' (here,")
    print("more experience roughly means more salary, colored by department).")
    print("Histogram answers a totally different question: 'what does the")
    print("spread of ONE variable look like?' — point out the kde=True curve")
    print("as a smoothed view of the same distribution.")
