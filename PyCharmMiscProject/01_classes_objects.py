"""
Master Class 4 — OOP Basics
Topic: Classes, Objects & __init__

Run me directly:  python 01_classes_objects.py
"""


class Model:
    def __init__(self, name, lr=0.01):
        self.name = name        # instance attribute
        self.lr = lr
        self.trained = False

    def train(self):
        self.trained = True
        print(f"{self.name} trained at lr={self.lr}")


# --- no 'new' keyword needed ---
m = Model("gpt-mini")
m.train()

print(m.name, m.lr, m.trained)

# A second, independent instance — proves state is per-object
m2 = Model("gpt-nano", 0.001)
print(m2.name, m2.lr, m2.trained)   # unaffected by m.train()


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("1. Calling Model(...) directly creates the instance — no 'new'.")
    print("2. self is explicit and must be the first parameter of every method.")
    print("3. m and m2 have completely independent .trained state.")
